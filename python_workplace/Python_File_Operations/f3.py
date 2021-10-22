def file_read(fname):
    with open(fname,"w") as myfile:
        myfile.write("Python Example for append \n")
        myfile.write("Python Exercies")
    txt=open(fname)
    print(txt.read())

file_read("te.txt")