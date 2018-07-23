from random import randint
goal = randint(1, 10)
guess = null

while guess != goal:
    guess = int(input('Guess a number between 1 and 10 \n'))
    if guess == goal:
        print('You guessed it! You won! \n')
        play-again = input('Would you like to play again? (y/n)')
        if play-again == 'y':
            guess = null
            goal = randint(1, 10)
    elif guess < goal:
        print('Too low, try again!')
    else:
        print('Too high, try again!')


