# need to install a driver, package which allows you to access database
import mysql.connector

cnx = mysql.connector.connect(user='root',
    password='Geogoog74!', #use user access from SQL workbench
    host='127.0.0.1', #own machine
    database='Farm',
    auth_plugin='mysql_native_password')

cursor = cnx.cursor()
query = ("INSERT INTO `Customers` VALUES ('kara','danvers','kara@mit.edu')")
cursor.execute(query)

#loop through data and print to terminal for SELECT 
for row in cursor.fetchall():
    print(row)

#clean up
cnx.commit()
cursor.close()
cnx.close() 
