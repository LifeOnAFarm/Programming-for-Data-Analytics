# Week 4 Lab
# Seamus de Cleir

import os

#1
# Creates text file and then reads it
with open("Week4Lab.txt", "w+") as f:
    f.write("Hello World\nThis is my text file\nIt's stores text etc. etc.\n")
    f.seek(0)
    print(f.read())

#2
# Appends to text file and then reads it
with open("Week4Lab.txt", "a+") as f:
    f.write("Hello World\nThis is my text file\nIt's stores text etc. etc.\n")
    f.seek(0)
    print(f.read())

#3
# Reads a text file and then copies it to a new file
with open("Week4LabNew.txt", "a+") as f:
    with open("Week4Lab.txt", "r") as f2:
        f.write(f2.read())
    f.seek(0)
    print(f.read())

# Removes the text files for debugging
#os.remove("Week4Lab.txt")
#os.remove("Week4LabNew.txt")