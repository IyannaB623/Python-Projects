import random

#score variables 
player_score = 0 
computer_score = 0

while True:

    player_choice = input("Rock, Paper, or Scissors?").lower()
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)

    print('You chose {}, and computer chose {}'.format(player_choice.capitalize(), computer_choice.capitalize()))

    if player_choice == computer_choice:
        print('Its a tie!')
    elif player_choice == 'rock':
            if computer_choice == 'paper':
                print('Its a wrap! You lose :(')
                computer_score += 1
            else:
                print('Nice! Rock beats Scissors!')
                player_score += 1
    elif player_choice == 'scissors':
            if computer_choice == 'rock':
                print('Rock Smashes Scissors! You lose!')
                computer_score += 1
            else:
                print('Nice! Scissors beats paper!')
                player_score += 1
    elif player_choice == 'paper':
            if computer_choice == 'scissors':
                print('Snip snip! You lose :(')
                computer_score += 1
            else: 
                print('Nice! Thats a wrap, paper beats rock!')
                player_score += 1
    else: 
        print('error')

    current_score = ('Your score is {}, and computer score is {}'.format(player_score, computer_score))
    print(current_score)

    try_again = input('Play again (Y/N)?').upper()

    if(try_again == 'N'):
            print('Thanks for playing!')
            break

