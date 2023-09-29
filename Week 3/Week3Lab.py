""" Week 3 Questions
    Seamus de Cleir"""

#Question 1: Built in Functions and Data Structures
txt = "Hello World"
#a
print(len(txt))
#b
print(txt[0])
#c
print(txt[1:4])
#d
print(txt[1:5])
#e
print((" Hello World ").strip())
#f
print(txt.upper())

#Question 2: Lists
#1
def addList(list1, list2):
    list3 =[]
    #If the lists match then add them together
    if len(list1)==len(list2):
        for idx, i in enumerate(list2):
            list3.append(list1[idx]+i)
    #If list1 is bigger add all the items together and then extend the bigger list
    elif len(list1)>len(list2):
        for idx, i in enumerate(list2):
            list3.append(list1[idx]+i)
        list3.extend(list1[len(list2):])
    #If list2 is bigger add all the items together and then extend the bigger list    
    else:
        for idx, i in enumerate(list1):
            list3.append(i+list2[idx])
        list3.extend(list1[len(list1):])
    return list3



list1 = ["M", "na", "i", "Ke","ke", 45]
list2 = ["y", "me", "s", "lly"]

print(addList(list1, list2))

#2
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# Add the lists
list1.extend(list2)

print(list1)

#Question 3: Dictionary
#1
#Takes two lists and creates a Dictionary 
def dicMaker(listA,listB):
    dic = {}
    for idx, i in enumerate(listA):
        dic[i] =listB[idx]
    return dic

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dicMaker(keys,values))

#2
sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70, "history":80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])

#3
# Return a new dictionary from a list and a dictionary
def dicExtractor(dict,lit):
    newdict = {}
    for i in lit:
        newdict[i] = dict[i]
    return newdict

sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
# Keys to extract
keys = ["name", "salary"]

print(dicExtractor(sample_dict,keys))

           