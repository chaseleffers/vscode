import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="support"
)

print(mydb)
