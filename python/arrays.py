targetNumber = 10

list1 = [2, 5, 6, 4, 10, 100]

'''
for x in list1:
    for y in list1:
        if (x == y):
            continue
        sum = x+y
        if sum==targetNumber:
            print("Found {} and {} have the sum {}".format(x, y, targetNumber))
            break
    else:
        continue
    break
'''

for x in list1:
    diff = targetNumber - x
    if diff in list1:
        print("Found {} and {}".format(x, diff))
        break