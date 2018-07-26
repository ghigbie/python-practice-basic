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

numbers.extend([8, 9, 10, 11, 12, 13])

for num in numbers:
    print(num)

print ('**********************') 

while count < len(numbers):
    print(numbers[count])
    count += 1
count = 0

print ('**********************')