import MySQLdb

try:
    query="delete from stdinfo where name='anirudha'"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stddbms_info")
    cur=mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print("\n Record deleted ....")
except:
    print("\n Record not deleted !!!!")
    
finally:
    cur.close()
    print("\n Cursor close...")            
    mycon.close()
    print("\n Mycon close...")      