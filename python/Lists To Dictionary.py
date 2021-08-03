import random

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

myNewList = list(zip(list1, list2))
myDict = {}
#print(myNewList)

for (key, value) in myNewList:
    myDict[key] = value

#print(myDict)
#print(random.choice(list(myDict.keys())))

#list3 = [x**2 for x in list1]

list3 = list(map(lambda x : x**2, list1))

#print(list3)

list4 = list(filter(lambda x : x%2==0, list1))
#print(list4)
#map(lambda (filter(lambda x:x%2==0)), list1)