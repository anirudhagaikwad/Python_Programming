#Program to create MYSQL connection

import mysql.connector #Import mysql.connector module

#Established Connection
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database="student")
print("\n Database Connection Established :: \n",myconn)

myconn.close()
