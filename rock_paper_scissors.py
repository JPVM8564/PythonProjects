import random

def rock_paper_scissors():

    choice = input("Make your choice: Rock, paper or scissors? ")

    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    if choice.lower() == "rock" and computer_choice == "rock":
        print("It's a tie!")
    elif choice.lower() == "rock" and computer_choice == "paper":
        print("Paper beats rock. Computer wins!")
    elif choice.lower() == "rock" and computer_choice == "scissors":
        print("Rock beats scissors. Player wins!")

    if choice.lower() == "paper" and computer_choice == "rock":
        print("Paper beats rock. Player wins!")
    elif choice.lower() == "paper" and computer_choice == "paper":
        print("It's a tie!")
    elif choice.lower() == "paper" and computer_choice == "scissors":
        print("Scissors beat paper. Computer wins!")

    if choice.lower() == "scissors" and computer_choice == "rock":
        print("Rock beats scissors. Computer wins!")
    elif choice.lower() == "scissors" and computer_choice == "paper":
        print("Scissors beat paper. Player wins!")
    elif choice.lower() == "scissors" and computer_choice == "scissors":
        print("It's a tie!")


#rock_paper_scissors()

##########################################################################################################################################

def play():
    user = input("Make your choice: (r) for Rock, (p) for paper or (s) for scissors? ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's a tie!")

    elif is_win(user, computer):
        print('You won!')
    else:
        print("You lost!")

def is_win(user, computer):
    if user == 'r' and computer == 's' or user == 'p' and computer == 'r' \
    or user == 's' and computer == 'p':
        return True
    
play()