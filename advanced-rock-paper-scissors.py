print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("Player 1, please choose one of the three choices: ").lower()
count = 0
while count < 20:
    print("* * * NO CHEATING * * *")
    count+=1
player2 = input("Player 2, please choose one of the three choices: ").lower()

win1 = "Player 1 wins!"
win2 = "Player 2 wins!"

if player1 == 'rock':
    if player2 == 'scissors':
        print(win1)
    if player2 == 'paper':
        print(win2)
elif player1 == 'paper':
    if player2 == 'scissors':
        print(win2)
    if player2 == 'rock:
        print(win1)
elif player1 == 'scissors':
    if player2 == 'rock':
        print(win2)
    if player2 == 'paper:
        print(win1)
elif player1 == player2
    print('There is a tie!')
else:
    print('Invalid choice. Please play again.')
