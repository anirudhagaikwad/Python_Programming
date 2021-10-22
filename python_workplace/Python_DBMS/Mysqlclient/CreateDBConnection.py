import MySQLdb

mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stddbms_info")
print("\n Database connection established :: ",mycon)
mycon.close()