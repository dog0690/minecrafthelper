import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database='testdatabase',
)
mycursor = db.cursor()

mycursor.execute("DROP DATABASE db")
mycursor.execute("DROP TABLE tb")