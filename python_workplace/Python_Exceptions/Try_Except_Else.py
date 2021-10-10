
try:
    c = open("abc.txt", 'r')
    print(c.read());
except IOError:
    print("Error in opening the file or the file doesn't exist");
else:
    print("File read successfully..!!");
    c.close()   