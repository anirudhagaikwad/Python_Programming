import MySQLdb

try:
    query="create table stdinfo(name varchar(50),birth varchar(50),address varchar(100))"
    #Established Connection
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stddbms_info")
    cur=mycon.cursor()
    cur.execute(query)
    print(query +" Sucessfully created")
except:
    print("Table Not Created")
finally:
    cur.close()
    print("\n Cursor close...")            
    mycon.close()
    print("\n Mycon close...")          