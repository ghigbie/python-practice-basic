age = int(input("How old are you? Please enter your age: "))

if age != ""
    if age >= 18:
        if age >= 21:
            print('You can drink and watch!')
        else:
            print('You can only watch')
    else:
        print('Go away youngster!')
else:
    print("Please enter an age")