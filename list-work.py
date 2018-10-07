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
stuffs = " ".join(stuff)
print(stuffs)
stuffs2 = "".join(stuff)
print(stuffs2)
print('********************')

cats = ['Blue', "Kicker", "Chubby", "Fluffy"]
print(cats)
cats.clear()
print(cats)
print('********************')

cats = ['Blue', "Kicker", "Chubby", "Fluffy"]
print(cats)
cats.pop()
print(cats)
cats.pop(0)
print(cats)
print('************************')

cats = ['Blue', "Kicker", "Chubby", "Fluffy", "Blue"]
print(cats)
cats.remove('Blue')
print(cats)
cats.remove(cats[2])
print(cats)
print('************************')