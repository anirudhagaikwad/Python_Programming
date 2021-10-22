import mysql.connector #Import mysql.connector module

try:
	query="create table stdinfo(name varchar(35),birth varchar(15),addr varchar(50))"
	#Established Connection
	myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database="Studentinfo")
	#Create Special Object of Cursor
	cur = myconn.cursor()
	cur.execute(query)#execute single query
	print("Table Created Successfully")
	

		

except mysql.connector.DatabaseError as err:
		if myconn!=None :
					myconn.rollback()
					print("\n Database Connection have issue : ",err)
			
finally :	
		cur.close()	
		print("\n Cursor Close")		
		myconn.close()	
		print("\n Connection Close")		
							

