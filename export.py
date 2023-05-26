import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="twInkbrush67",
  database="splat_tweets_learnset"
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