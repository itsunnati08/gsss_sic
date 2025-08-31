list1 = [7, 19, 13, 5]
list2 = [2, 3, 13]

print(list1.extend(list2)) # [7, 19, 13, 5, 2, 3, 13]
print(list1)
list1.append(list2) # [7, 19, 13, 5, [2, 3, 13] ]
print(list1)
print(list1 + list2) # [7, 19, 13, 5, 2, 3, 13]
print(list1 * 3) # [7, 19, 13, 5, 7, 19, 13, 5, 7, 19, 13, 5]
print(7 in list1) # True
print(17 in list1) # False
print(7 not in list1) # False
print(17 not in list1) # True