import mysql.connector
connc=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="telebot"
    )
prop=connc.cursor()


