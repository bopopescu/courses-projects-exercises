import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="qbasuperfly",
  passwd="Kuba1987"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

