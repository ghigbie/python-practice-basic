from random import randint
goal = randint(1, 10)
guess = None

while guess != goal:
    guess = int(input('Guess a number between 1 and 10 \n'))
    if guess == goal:
        print('You guessed it! You won! \n')
        play_again = input('Would you like to play again? (y/n)')
        if play_again == 'y':
            guess = None
            goal = randint(1, 10)
        else:
            print('Thanks for playing : )')
            break
    elif guess < goal:
        print('Too low, try again!')
    else:
        print('Too high, try again!')


