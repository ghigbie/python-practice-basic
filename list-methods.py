numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

print ('**********************')

count = 0
while count < len(numbers):
    print(numbers[count])
    count += 1
count = 0

print ('**********************')
#append will addd a single item to the end of a list
numbers.append(6)
numbers.append(7)

for num in numbers:
    print(num)

print ('**********************')

while count < len(numbers):
    print(numbers[count])
    count += 1
count = 0 

print ('**********************')
#extend will add another list to the end of a list
numbers.extend([8, 9, 10, 11, 12, 13])

for num in numbers:
    print(num)

print ('**********************') 

while count < len(numbers):
    print(numbers[count])
    count += 1
count = 0

print ('**********************')

#insert will add an item at a specific place in a list
numbers.insert(3, 'Yo!')
numbers.insert(7, 'Yo2!')

for num in numbers:
    print(num)

print ('**********************')

for num in numbers:
    print(numbers[count])
    count += 1
count = 0

print ('**********************')
# clear will remove all items from a list
numbers.clear()
print ('**********************')
print ('**********************')
for num in numbers:
    print(num)
print ('**********************')
print ('**********************')

numbers = [1, 2, 3, 4, 5]
numbers.extend([6, 7, 8, 9, 10, 11, 12, 13, 14])

for num in numbers:
    print(num)

print ('**********************')

numbers.pop()
for num in numbers:
    print(num)
print ('**********************')
numbers.pop(0)
for num in numbers:
    print(num)
print ('**********************')

numbers.append('yellow')

for num in numbers:
    print(num)

print ('**********************')
#removes a specified value
numbers.remove('yellow')

for num in numbers:
    print(num)

print ('**********************')
# provides the index of a value
val = numbers.index(11)
print(val)

print('*********************')
#reverse changes the order of a list

numbers.reverse()
for num in numbers:
    print(num)

print ('**********************')
#sorts a list in asscending order
numbers.sort()


for num in numbers:
    print(num)

print ('**********************')

#joins all the items in a list in to a string
# string-val = ", ".join(numbers)
# print(numbers)


print ('**********************')
#slice functions
print(numbers[::])
print(numbers[4:8])
print(numbers[0:12:2])
print(numbers[::-1])
print(numbers[::-2])
print(numbers[::-3])
print('redrum'[::-1])
print ('**********************')

#comma syntax for switching items in list
colors = ['red', 'blue', 'green']
print(colors)
colors[0], colors[1] = colors[1], colors[0]
print(colors)
print ('**********************')
#joins strings only in a list
print('...'.join(colors))
print ('**********************')
# List comprehension
ten_numbers = [x*10 for x in numbers]
print(ten_numbers)
halfnumbers = [x/2 for x in numbers]
print(halfnumbers)
print([color.upper() for color in colors])
print(colors)
print([bool(color) for color in colors])
new_numbers = [0, 1, 0, 2, 0, 3, 0, 4]
print([bool(new) for new in new_numbers])
print ('**********************')
#List Comprehension with conditionals
print([num for num in numbers if num % 2 == 0])
print([num for num in numbers if num % 2 == 1])
print([color for color in colors if color == 'red'])
print([color for color in colors if color == 'blue'])
print([num*2 if num % 2 == 0 else num/2 for num in numbers])
print([color.upper() if color == 'red' else color for color in colors])
print([color.upper() if color == 'blue' else color for color in colors])
print([color.upper() if color == 'green' else color for color in colors])
print ('**********************')