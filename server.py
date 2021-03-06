import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vtrack"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM map_vehicle")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)