from random import randint
options = ['rock', 'paper', 'scissors']
player_wins = 0
computer_wins = 0
winning_score = 2
win1 = "Player 1 wins!"
win2 = "Computer wins!"
comp_random_option = options[randint(0,2)]
computer_choice = f"Computer chooses {comp_random_option}."

while player_wins < winning_score and computer_wins < winning_score:
    for option in options:
        print(f"...{option}...")
    print(f'Total score: Player {player_wins} / Computer {computer_wins}')
    player1 = input("Player 1, please choose one of the three choices: ").lower()
    if player1 == 'quit' or player1 == 'q':
        break
    if player1 == comp_random_option:
        print('There is a tie!')
    elif player1 == 'rock':
        if comp_random_option == 'scissors':
            print(computer_choice, win1)
            player_wins += 1
        elif comp_random_option == 'paper':
            print(computer_choice, win2)
            computer_wins += 1
    elif player1 == 'paper':
        if comp_random_option == 'scissors':
            print(computer_choice, win2)
            computer_wins += 1
        elif comp_random_option == 'rock':
            print(computer_choice, win1)
            player_wins += 1
    elif player1 == 'scissors':
        if comp_random_option == 'rock':
            print(computer_choice, win2)
            computer_wins += 1
        elif comp_random_option == 'paper':
            print(computer_choice, win1)
            player_wins += 1
    else:
        print('Invalid choice. Please play again.')


print(f'FINAL SCORE: Player {player_wins} / Computer {computer_wins}')

if player_wins > computer_wins:
    print('Congratulations! You won!')
else:
    print('Sorry please try again')