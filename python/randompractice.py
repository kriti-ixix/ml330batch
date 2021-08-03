import random as r
'''
x = r.randint(1,100)
print("randint:", x)

y = r.random()
print("random: ", y)

z = r.uniform(1,10)
print("uniform: ", z)
'''
myList = [1, 2, 3, 4, 5, 6, "x", 10.5, True, "Hello World"]
'''
print("choice: ", r.choice(myList))

print(myList[6])
print(myList[8])
print(myList[-1])
print(myList[-3])
print(myList[::-1])
print(myList[3:])

print(r.choice("Hello"))

if 'x' in myList:
    print("x found in the list")

if 5 not in myList:
    print("5 is not in the list")
else:
    print("5 found in the list")

for num in myList:
    print(num, end=" and ")
'''

for x in "Hello":
    print(x)
