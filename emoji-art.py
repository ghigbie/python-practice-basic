emoji = "\U0001f600"
count = 0
stop = 21

while count < stop:
    print(emoji * count)
    count += 1

print("*************************")

numbers = range(1, 21)
for num in numbers:
    print(emoji * num)