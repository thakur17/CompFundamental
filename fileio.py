#Today, we are going to learn about file I/O
#w for overwrite and a for append

file = open("mylovelyfile", "a")
file.write("Now the file has more content!")
file.write("This is the second line going into the file")

file.close()

#open and read the file after the appending:
f = open("mylovelyfile", "r")
print(f.read())
f.close()

import os #This imports the Operating System library
os.remove("mylovelyfile")


    
