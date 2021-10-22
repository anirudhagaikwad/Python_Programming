import MySQLdb #Import MySQLdb module

try:
	query="create Database Studentinfo"
	#Established Connection
	myconn = MySQLdb.connect(host = "localhost", user = "root",passwd = "")
	#Create Special Object of Cursor
	cur = myconn.cursor()
	cur.execute(query)#execute single query
	print("Database Created Successfully")
	

		

except:
		if myconn!=None :
					myconn.rollback()
					print("\n Database Connection have issue : ")
			
finally :	
		cur.close()	
		print("\n Cursor Close")		
		myconn.close()	
		print("\n Connection Close")		
							

