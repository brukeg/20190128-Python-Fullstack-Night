# rps.py
import random

def calc_winner(comp_choice, user_choice):  
    """
    returns winner based on comp_choice and user_choice
    """
    # defeats is a dictionary with key=choice, value=what the key defeats
    defeats = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if comp_choice == user_choice:
        return 'Tie'
    elif defeats[comp_choice] == user_choice:
        # if comp_choice defeats user_choice
        return 'Computer wins'
    else: # elif defeats[comp_choice] != user_choice
        return 'User wins'

rps = ['rock', 'paper', 'scissors']
while True: # loop game until user wants to stop
    while True: # input validation
        user_choice = input('Rock, paper, or scissors: ').strip().lower()
        if user_choice in rps:
            break
    computer_choice = random.choice(rps)
    print(computer_choice)
    print(calc_winner(computer_choice, user_choice))

    while True: # input validation
        play_again = input('Do you want to play again: ').strip().lower()
        if play_again in ['y', 'yes', 'n', 'no']:
            break 

    if play_again.startswith('n'):
        break

# You can test your logic by passing test inputs into your function
# This is easier to test than working with random inputs
# print(calc_winner('rock', 'rock'))
# print(calc_winner('rock', 'paper'))
# print(calc_winner('rock', 'scissors'))
# print(calc_winner('paper', 'rock'))
# print(calc_winner('paper', 'paper'))
# print(calc_winner('paper', 'scissors'))
# print(calc_winner('scissors', 'rock'))
# print(calc_winner('scissors', 'paper'))
# print(calc_winner('scissors', 'scissors'))