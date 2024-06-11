# create a simple rock-paper-scissors game
# provide a welcome message followed by the rules of the game
# ask the user to choose rock, paper, or scissors
# randomly generate the computer's choice
# in case of a tie, print "It's a tie!" and ask the user to play again
# if the user wins, print "You win!" and ask the user to play again
# if the computer wins, print "You lose!" and ask the user to play again
# if the user chooses an invalid option, print "Invalid option!" and ask the user to play again
# provide a goodbye message when the user decides to stop playing
# use a while loop to keep the game running until the user decides to stop playing
# store the scores of the user and the computer and print the scores after each round
# apart from the goodbye message, print the final scores of the user and the computer on a table after the user decides to stop playing

import random

def play_round(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", 1, 0
    else:
        return "You lose!", 0, 1

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock")

    user_score = 0
    computer_score = 0

    while True:
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to stop playing: ")
        while user_choice not in choices and user_choice != 'quit':
            print("Invalid option!")
            user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to stop playing: ")

        if user_choice == 'quit':
            break

        print("Computer chose: ", computer_choice)

        result, user_round_score, computer_round_score = play_round(user_choice, computer_choice)
        print(result)
        user_score += user_round_score
        computer_score += computer_round_score

        print(f"Scores:\nUser: {user_score}\nComputer: {computer_score}")

    print("Thanks for playing! Here are the final scores:")
    print(f"User: {user_score}\nComputer: {computer_score}")

rock_paper_scissors()



