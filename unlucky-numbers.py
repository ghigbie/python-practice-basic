numbers = range(1, 21)


for number in numbers:
    if number == 4 or number == 13:
        print(f"{number} is UNLUCKY")
    elif number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
