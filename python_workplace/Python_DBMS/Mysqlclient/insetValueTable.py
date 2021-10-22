import MySQLdb

try:
    #create table stdinfo(name varchar(50),birth varchar(50),address varchar(100))
    query="insert into stdinfo values('anirudha','15July1985','Solapur')"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stddbms_info")
    cur=mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print(query+" :: Value insterd sucessfully")
except:
    print("Value not inserted in table")    
finally:
    cur.close()
    print("\n Cursor close...")            
    mycon.close()
    print("\n Mycon close...")     