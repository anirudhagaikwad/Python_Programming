def something():
    print("this fun from script1...")

if __name__ == '__main__':
    something() 
    print("call from script1...")
else:
    print("script1 is imported in some other file...")
