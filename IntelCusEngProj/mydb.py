import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE inteldbtable")

print("Database Connected Successfully!")