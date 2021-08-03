'''
#print("Hello World")

#x = 5 
#print(x)
#print(type(x))

#y = 5.5
#print(type(y))
#x = 10
#print(x)

#z = 'Hello'
#print(type(z))

#a = False 
#print(type(a))

#This is a code about ....

This is a 
multi line 
comment

x = 10
y = str(x)
print(type(x))
print(type(y))

print(4==4)
print(3==4)


s = "Hello World"

#Concatenation
t = " I'm Kriti"

x = "Hello #Sports"

#print(s+t)

#print(len(s+t))

#print(s.upper())

#print(x.split("o"))

print(s*20)


def printOut():
    print("Hi")

   
printOut()
printOut()
printOut()
printOut()


def addTwoNums(a, b):
    return a+b


x = addTwoNums(10, 20)
 
y = x*10

print(y)

x = int(input("Enter your marks here: "))

if x>70 and x<=100:
    print("Good")

elif x>=50 and x<=70:
    print("Average")

elif x<50 and x>0:
    print("Poor")

else:
    print("Invalid input")
'''


b = [1,2,3,4,5]
l = len(b)

for x in b:
    if (len(b)==l*2):
        break
    print(x)
    x = x+1
    print("After adding: ", x)
    b.append(x)

print(b)