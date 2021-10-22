import mysql.connector #Import mysql.connector module
			
try:
	#query="create table stdinfo(name varchar(35),birth varchar(15),addr varchar(50))"
	#Established Connection
	myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database="studentinfo")
	#Create Special Object of Cursor
	cur = myconn.cursor()
	query="select * from stdinfo"
	cur.execute(query)#execute single query
	Tdata=cur.fetchall()
	print("\n Record from Table : ")
	for row in Tdata:
						print("\n Student Name :",row[0])
						print("\n Student BirthDate :",row[1])
						print("\n Student Address :",row[2])
						
						

	
			
				
except mysql.connector.DatabaseError as err:
		if myconn!=None :
					myconn.rollback()
					print("\n Database Connection have issue : ",err)
			
finally :	
		cur.close()		
		myconn.close()		
							

