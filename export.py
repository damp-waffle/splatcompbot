import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
db = mysql.connector.connect(
  host=os.getenv('SERVER_NAME'),
  user=os.getenv('USERNAME'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DB_NAME')
)
mycursor = db.cursor()
mycursor.execute("SELECT text FROM tweets")

myresult = mycursor.fetchall()
f=open("trainingdata.jsonl", "w")
f.close()
f=open("trainingdata.jsonl", "a")
for x in myresult:
    f.write('{"prompt":"","completion":" ' + str(x)[2:-3].encode("unicode_escape").decode("utf-8").replace('"','\\"') + '"}')
    if(x != myresult[len(myresult)-1]):
        f.write("\n")