emoji = "\U0001f600"
count = 0
stop = 21

while count < stop:
    print(emoji * count)
    count += 1

print("*************************")

numbers = range(1, stop)
for num in numbers:
    print(emoji * num)

numbers2 = range(1, 10)
for num in range(5):
    for num in numbers2:
        print(emoji * num)