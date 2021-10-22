with open('te.txt','r+') as f: 
    f.write("afafaafafsdgsdgsdgsghello content 443....")
    f.close()
with open('te.txt','r+') as ff:     
    for line in ff:
        print(line.strip())



