from random import randint
options = ['rock', 'paper', 'scissors']
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    for option in options:
        print(f"...{option}...")
    print(f'Total score: Player {player_wins} / Computer {computer_wins}')
    comp_random_option = options[randint(0,2)]

    player1 = input("Player 1, please choose one of the three choices: ").lower()
    # while player1 != options[0] or player1 != options[1] or player1 != options[2]:
    #     print("You ented an invalid choice.")
    #     player1 = input("Player 1, please choose one of the three choices: ").lower()

    win1 = "Player 1 wins!"
    win2 = "Computer wins!"
    computer_choice = f"Computer chooses {comp_random_option}."

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