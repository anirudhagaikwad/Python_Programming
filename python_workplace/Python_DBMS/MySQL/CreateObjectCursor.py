#Program to Create Special Object of Cursor

import mysql.connector #Import mysql.connector module

#Established Connection
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database="student")
print("\n Database Connection Established :: \n",myconn)

#Create Special Object of Cursor
cur = myconn.cursor()
print("\n Cursor Object Created :: \n",cur)
cur.close()
myconn.close()