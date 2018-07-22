numbers = range(20)


for number in numbers:
    if number == 4 or number == 13:
        print(f"{number} is unlucky")
    elif number % 2 == 1:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
