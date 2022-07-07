import pyinputplus as pyin
import random

def rock():
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    return True

def paper():
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    return True

def scissors():
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
    return True

def checkRules(player_choice, computer_choice):
    if(player_choice == 'Rock' and computer_choice == 0):
        print("Draw!")
    elif(player_choice == 'Rock' and computer_choice == 1):
        print("Player 1 loses!")
    elif(player_choice == 'Rock' and computer_choice == 2):
        print("Player 1 wins!")
    elif(player_choice == 'Paper' and computer_choice == 0):
        print("Player 1 wins!")
    elif(player_choice == 'Paper' and computer_choice == 1):
        print("Draw!")
    elif(player_choice == 'Paper' and computer_choice == 2):
        print("Player 1 loses!")
    elif(player_choice == 'Scissors' and computer_choice == 0):
        print("Player 1 loses!")
    elif(player_choice == 'Scissors' and computer_choice == 1):
        print("Player 1 wins!")
    elif(player_choice == 'Scissors' and computer_choice == 2):
        print("Draw!")

choice = pyin.inputChoice(['Rock', 'Paper', 'Scissors'],caseSensitive=False)
print("Player 1: ")
if choice.lower() == 'rock':
    rock()
elif choice.lower() == 'paper':
    paper()
else:
    scissors()

computerChoice = random.randint(0,2)
print("Computer: ")
if computerChoice == 0:
    rock()
elif computerChoice == 1:
    paper()
else:
    scissors()

checkRules(choice, computerChoice)