colors =  ['red', 'magenta', 'yellow', 'orange', 'green']

for color in colors:
    print(color)

numbers = [4, 6, 8, 10, 12, 14 , 16, 18]

for num in numbers:
    print(num * num)

print('***************************')
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print('**************************')

i = 0
while i < len(colors):
    print(f"At index {i} the color is {colors[i]}")
    i += 1

print('************************')
result = ''
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
for sound in sounds:
    result += sound

print(result.upper())

print('********************')

stuff = ['books', 'dvds', 'computers']
stuff = " ".join(stuff)
print('********************')
