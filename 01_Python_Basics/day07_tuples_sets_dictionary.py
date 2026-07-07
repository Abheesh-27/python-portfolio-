print('===== TUPLES =====')
items = ('Phone', 'Watch', 'Phone', 'Laptop', 'Shoes')
items1 = ('Battery' , 'Fuel', 'Charge')

print()

print(items)
print(type(items))

print()

#printing first item.
print('First element is: ',items[0])

#printing last item.
print('Last element is: ',items[-1])
print()

#printing length of tuple.
print('Length of the tuple is: ',len(items))
print()

#counting number of times element has repeated.
print('Phone appears',items.count('Phone'),'times in the tuple.')
print()

#finding postion of element.
print('Position of Laptop is: ', items.index('Laptop'))
print()

#concatinating 2 tuples.
concat = items + items1
print('New Tuple: ', concat)
print()

#checking if element exists in the tuple
print('Cats' in items)
print()

#finding items in tuple.
print("Items in the tuple: ")

for item in concat:
    print(item)

print()


print('===== SETS =====')
print()
set1 = {13,45,32,57}
set2 = {1,2,3}
set3 = {3,4,5}

print(set1)

# Adding an element
set1.add(95)
print("\nAfter adding 95:", set1)
print()

# Removing an element
set1.remove(32)
print("After removing 32:", set1)
print()

# pop() removes random element since sets are unordered.
set1.pop()
print("After pop():", set1)
print()

#union of sets.
print('Union of the sets are: ', set1 | set2 | set3)
print()

#intersection of the sets.
print('Intersection of the sets: ', set2 & set3)
print()

#difference of sets.
print('Difference is: ', set1 - set2)
print()

#symmetric difference.
print('Symmetric Difference of sets: ', set1 ^ set3)
print()

#finding elements in the set.
print("Elements in the set: ")

for element in set1:
    print(element)

print()


print('===== DICTIONARY =====')
print()

student = {
    'name' : 'Abheesh',
    'age' : 20,
    'department' : 'Civil'
}
print(student)
print(student['age'])
print(student.get('department'))
print()

#adding an item
student['college'] = 'IIT Madras'
print('Dictionary after adding college: ', student)
print()

#updating an item
student['age'] = 21
print('Dictionary after editing age: ', student)
print()

#deleting an item
del student['department']
print('Dictionary after deleting department: ', student)
print()

#finding the keys , values and items in dictionary
print("Dictionary Keys:", student.keys())
print("Dictionary Values:", student.values())
print('Dictionary Items: ',student.items())
print()

#Iterating through dictionary key-value pairs
for key,value in student.items():
    print(key , '=', value)
print()

#checking dictionary membership
print("Is 'age' a key in the dictionary?", 'age' in student)
print()