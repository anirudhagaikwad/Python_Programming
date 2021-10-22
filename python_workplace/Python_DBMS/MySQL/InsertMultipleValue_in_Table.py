import mysql.connector #Import mysql.connector module
			
try:
	#query="create table stdinfo(name varchar(35),birth varchar(15),addr varchar(50))"
	#Established Connection
	myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database="studentinfo")
	#Create Special Object of Cursor
	cur = myconn.cursor()
	while True:
				n=input("\n Enter Student Name : ")
				b=input("\n Enter Student Birthdate : ")
				a=input("\n Enter Student Address : ")
				query="insert into stdinfo values('%s','%s','%s')"
				cur.execute(query %(n,b,a)) 
				myconn.commit()
				#print("\n Records inserted Sucessfully : ")
				choice=input("\n Do you want to Add more Student : Y/N ::")
				if choice=='N':
								break
						
except mysql.connector.DatabaseError as err:
		if myconn!=None :
					myconn.rollback()
					print("\n Database Connection have issue : ",err)
			
finally :	
		cur.close()		
		myconn.close()		
							

