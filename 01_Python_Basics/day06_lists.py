# Day 6 - Lists 

numbers = []

for i in range(5):
    n = int (input('Enter a number: '))
    numbers.append(n)

print('\n Given list is: ',numbers)

#sorting the list.
numbers.sort()
print('\n Sorted list: ',numbers)

#maximum and minimum of the list.
print('\n Largest number: ',max(numbers))
print('\n Smallest number: ',min(numbers))

#finding average of the list.
average = sum(numbers) / len(numbers)
print('\n Average: ', average)

#reversing the list.
numbers.reverse()
print('\n Reversed list: ',numbers)

#removing last element in the list.
removed = numbers.pop()
print('\n Removed element: ',removed)
print('\n New List: ',numbers)

#slicing the list.
print('\n Edited List: ',numbers[1:3])
print('\n Edited list 2: ',numbers[::3])

print()

#removing the 2nd element.
numbers.pop(1)
print('\n New list 3: ',numbers)

#removing the largest element.
numbers.remove(max(numbers))
print('\n New list 4: ',numbers)


