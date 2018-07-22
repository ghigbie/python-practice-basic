print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Player 1, please choose one of the three choices: ").lower()
if player1 != 'rock' or player1 != 'paper' or player1 != 'scissors':
    print('You entered an invalid choice.')
    player1 = input("Player 1, please choose one of the three choices: ").lower()

count = 0
while count < 20:
    print("* * * NO CHEATING * * *")
    count+=1
player2 = input("Player 2, please choose one of the three choices: ").lower()
if player2 != 'rock' or player2 != 'paper' or player2 != 'scissors':
    print('You entered an invalid choice.')
    player2 = input("Player 2, please choose one of the three choices: ").lower()

win1 = "Player 1 wins!"
win2 = "Player 2 wins!"
if player1 == player2:
    print('There is a tie!')
elif player1 == 'rock' and player2 == 'scissors':
    print(win1)
elif player1 == 'paper' and player2 == 'rock':
    print(win1)
elif player1 == 'scissors' and player2 == 'paper':
    print(win1)
elif player2 == 'rock' and player1 == 'scissors':
    print(win2)
elif player2 == 'paper' and player1== 'rock':
    print(win2)
elif player2 == 'scissors' and player1 == 'paper':
    print(win2)
else:
    print('Invalid choice. Please play again.')
