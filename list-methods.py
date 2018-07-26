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