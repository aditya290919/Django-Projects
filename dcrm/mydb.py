import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'aditya',
	passwd = 'aditya@29',


	)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE metho")

print("ALL Done")