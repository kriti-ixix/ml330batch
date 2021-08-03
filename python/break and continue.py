'''
myList = list(range(1,101))
print(myList)

print(myList)
oddcounter = 0
evencounter = 0

for num in myList:
    if (num%2==0):
        evencounter+=1
    else:
        oddcounter+=1

print("Odd numbers: ", oddcounter)
print("Even numbers: ", evencounter)

myDict = {num:num**2 for num in myList}

for num in myList:
    myDict[num] = num**2

print(myDict)
'''

myList = list(range(101))

for x in myList:
    print(x)