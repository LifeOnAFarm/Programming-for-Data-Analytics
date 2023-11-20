"""
Name:   Seamus de Cleir
ID:     x22128956
Course: Programming for Data Analytics
Date:   20/11/20023

"""

import random

# Question 1
#1
x = 22128956 % 5

#2
random.seed(22128956)
y = random.randint(0,9)

# Question 2
#1 #2 #3 & #4 

with open("ca1_input.txt","r") as readFile, open("ca1_output.txt","w") as outFile:
    line = readFile.readlines()
    txtLine = line[x+1]

    words = txtLine.split()

    for i in words:
        print(i[-1])
        outFile.write(i[-1])

# Question 3
#1 #2
userAge = -1
while (userAge < 0) or (userAge > 99):
    try:
        userAge = int(input("What is your age in years?"))
        if (userAge < 0) or (userAge > 99):
            print("You can not be older than 100 or younger than 0!")
    except:
        print("Please input a number")

#3
for i in range(userAge,1000):
    if i % y == 0:
        print(i)

# Question 4
#1 #2 #3
def twoString(fstStr, sndStr):
    
    if not all(isinstance(i,str) for i in [fstStr,sndStr]):
        errorWord =  fstStr if not(isinstance(fstStr,str)) else sndStr
        print(f"{errorWord} is not a string")
        return
    
    strDic = {}
    longWord, shortWord = (fstStr, sndStr) if len(fstStr) > len(sndStr) else (sndStr, fstStr)

    for i in shortWord:
            strDic[i] = longWord
    
    return strDic

#4
my_name_dict = twoString("Seamus", "deCleir")
print(my_name_dict)