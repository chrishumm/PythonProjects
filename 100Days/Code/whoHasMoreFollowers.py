import random
import pyinputplus as pyin

NAME = {"Chris" : 100, 'George' : 2000, 'Michael' : 321, 'Frank' : 111}
LIST_OF_NAMES = ['Chris', 'George', 'Michael', 'Frank']
def calculate(playera, playerb, choice):
    if NAME[playera] < NAME[playerb] and choice == 'a':
        print(f"You lose {playera} has {NAME[playera]} followers, but {playerb} has {NAME[playerb]}")
        return
    elif NAME[playera] > NAME[playerb] and choice == 'a':
        print(f"You win {playera} has {NAME[playera]} followers, but {playerb} has {NAME[playerb]}")
        return

    if NAME[playera] < NAME[playerb] and choice == 'b':
        print(f"You win {playerb} has {NAME[playerb]} followers, but {playera} has {NAME[playera]}")
        return
    elif NAME[playera] > NAME[playerb] and choice == 'b':
        print(f"You lose {playerb} has {NAME[playera]} followers, but {playerb} has {NAME[playera]}")
        return

while True:
    player_a = random.choice(LIST_OF_NAMES)
    player_b = random.choice(LIST_OF_NAMES)
    if(player_a != player_b):
        break

choice = input("Who has more followers?\nA)  "+player_a+"\nB)  "+player_b+ ":  ")
calculate(player_a, player_b, choice)