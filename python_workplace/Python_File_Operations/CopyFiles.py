# Python Program - Copy Files

from shutil import copyfile;
print("Enter 'x' for exit.")
sourcefile = input("Enter source file name (copy from): ")
if sourcefile == 'x':
    exit()
else:
    destinationfile = input("Enter destination file name (copy to): ")
    copyfile(sourcefile, destinationfile)
    print("File copied successfully!")
    print("Want to display the content ? (y/n): ")
    check = input()
    if check == 'n':
        exit()
    else:
        c = open(destinationfile, "r")
        print(c.read())
        c.close()