import MySQLdb

try:
    query="select * from stdinfo"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stddbms_info")
    cur=mycon.cursor()
    cur.execute(query)
    tdata=cur.fetchall()
    print("\n Record from table : ")
    for row in tdata:
        print("\n student name : ",row[0])
        print("\n student bithdate : ",row[1])
        print("\n student address : ",row[2])
except:
    print("Value not fetch from  table")    
finally:
    cur.close()
    print("\n Cursor close...")            
    mycon.close()
    print("\n Mycon close...")            
