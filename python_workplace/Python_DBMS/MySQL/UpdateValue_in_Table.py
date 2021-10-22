import mysql.connector #Import mysql.connector module
			
try:
	#query="create table stdinfo(name varchar(35),birth varchar(15),addr varchar(50))"
	#Established Connection
	myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database="studentinfo")
	#Create Special Object of Cursor
	cur = myconn.cursor()
	query=" update stdinfo set birth='1june2016' where name='Vaishnavi'"
	cur.execute(query)#execute single query
	myconn.commit()
	print("\n Record inserted Sucessfully : ")
			
						
except mysql.connector.DatabaseError as err:
		if myconn!=None :
					myconn.rollback()
					print("\n Database Connection have issue : ",err)
			
finally :	
		cur.close()		
		myconn.close()		
							

