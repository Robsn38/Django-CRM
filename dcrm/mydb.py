import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '#19StPauli10'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dbDCRM")

print('Well done')