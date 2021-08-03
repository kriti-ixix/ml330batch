dict1 = {1:1, 2:9, 3:4, 4:10, 5:2}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get, reverse=True)
print(sorted_keys)

for x in sorted_keys:
    if sorted_keys.index(x)==3:
        break
    key = x 
    value = dict1[x]
    sorted_dict[key] = value

print(sorted_dict)
