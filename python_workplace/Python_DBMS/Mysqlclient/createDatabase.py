# Create Database

#import mysql.connector

import MySQLdb

try:
    query="create database stddbms_info"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="")
    cur=mycon.cursor()
    cur.execute(query)
except :
    if mycon!=None:
        mycon.rollback()
        print("Database connection have some issues....")
finally:
    cur.close()
    print("\n Cursor close...")            
    mycon.close()
    print("\n Mycon close...")            
