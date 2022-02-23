# need to install a driver, package which allows you to access database
import mysql.connector

cnx = mysql.connector.connect(user='root',
    password='Geogoog74!', #use user access from SQL workbench
    host='127.0.0.1', #own machine
    database='sys',
    auth_plugin='mysql_native_password')

cursor = cnx.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)

#loop through data and print to terminal
for row in cursor.fetchall():
    print(row)

#clean up
cursor.close()
cnx.close() 
