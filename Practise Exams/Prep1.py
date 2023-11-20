"""
Name:   Seamus de Cleir
ID:     x22128956
Course: Programming for Data Analytics
Date:   20/11/20023

"""

# Question 1
x = 22128956 % 10

#  Question 3
#1

# Create user input variable
userNum = 0

# Checks if the user input is between 10 and 19
while (userNum < 10) or (userNum > 19):
    try:
        userNum = int(input("Input a number betwen 10 and 19:"))
        if (userNum < 10) or (userNum > 19):
            print("Invalid number.Input a number betwen 10 and 19:")
    except:
        # If the vaild can not be cast to an int then reject it
        print("Invalid input.Please enter an integer")


#2
# Loop through the range and output odd numbers. Add 1 to userNum to make it inclusive
for i in range(x,userNum+1):
    if i % 2 != 0:
        print(i)

#3
with open("ca1_preparation.txt","w") as txtFile:
    txtFile.write(f"The difference between the two numbers is {userNum - x}")

