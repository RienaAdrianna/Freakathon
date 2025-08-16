import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    grocery="root",
    passwd = "grocery123",
    )

my_cursor = mydb.cursor()