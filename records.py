import os
import mysql.connector
from request import requestTweet
from dotenv import load_dotenv

load_dotenv()
db = mysql.connector.connect(
  host=os.getenv('SERVER_NAME'),
  user=os.getenv('USERNAME'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DB_NAME')
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM new_tweets")

myresult = mycursor.fetchall()
sql = "INSERT INTO tweets(id, text, author_id) VALUES (%s, %s, %s)"
success = 0
for x in myresult:
    resp = requestTweet(str(x)[2:-3])
    if(resp == ""):
        pass
    else:
        success += 1
        val = (resp['id'],resp['text'],resp['author'])
        mycursor.execute("SELECT * FROM author WHERE author_id = '" + resp['author'] +"'")
        res = mycursor.fetchone()
        if(res == None):
            mycursor.execute("INSERT INTO author(author_id, username) VALUES(%s, %s)", (resp['author'],resp['username']))
            db.commit()
        try:
            mycursor.execute(sql, val)
            db.commit()
        except:
            success -= 1
    delete = "DELETE FROM new_tweets WHERE url='" + str(x)[2:-3] + "'"
    mycursor.execute(delete)
    db.commit()

print("Summary: " + str(success)+ "/" + str(len(myresult)) + " added to database.")