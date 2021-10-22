import MySQLdb

try:
    query="update stdinfo set birth='18july1988' where name='anirudha'"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stddbms_info")
    cur=mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print("\n Record updated sucessfully")
except:
    print("\n Record not updated !!!!")
    
finally:
    cur.close()
    print("\n Cursor close...")            
    mycon.close()
    print("\n Mycon close...")   