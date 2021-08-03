filename = "Hello World.txt"
myFile = open(filename, 'w')

for x in range(5):
    myFile.write(input() + "\n")

myFileReading = open(filename, 'r')
print(myFileReading.read())

myFile.close()