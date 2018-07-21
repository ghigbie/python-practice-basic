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
if player1 == 'rock' and player2 == 'paper':
    print(win1)
elif player1 == 'paper' and player2 == 'rock':
    print(win1)
elif player1 == 'scissors' and player2 == 'paper':
    print(win1)
if player2 == 'rock' and player1 == 'paper':
    print(win2)
elif player2 == 'paper' and player1== 'rock':
    print(win2)
elif player2 == 'scissors' and player1 == 'paper':
    print(win2)
else:
    print('Invalid choice. Please play again.')
