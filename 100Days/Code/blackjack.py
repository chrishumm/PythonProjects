import random


def printMenu():
    print(''' _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                        _/ |                
                        |__/                 
    ''')
def dealCard():
    card = str(random.randint(1,10))
    special_cards = ['K', 'Q', 'J', '10']
    if card == '10':
        card = random.choice(special_cards)
    elif(card == 1):
        card = 'A'

    return card

def printHands(playersHand, computersHand):
    printMenu()
    print("The dealer has: ", end="")
    for i in range(len(computersHand)):
        print("|"+computersHand[i]+"|" ,end="")
    
    print("\n")

    print("The player has: ", end="")
    for i in range(len(playersHand)):
        print("|"+playersHand[i]+"|", end="")

    print("\n")


def calculateHands(hand):
    sum = 0
    for i in range(len(hand)):
        if(hand[i] == 'K' or hand[i] == 'J' or hand[i] == 'Q'):
            sum += 10
        elif(hand[i] == 'A'):
            sum += 10
        else:
            sum += int(hand[i])
        
    if 'A' in hand and sum > 21:
        return sum - 11

    return sum

def dealerPlay(player, computer):
    while True:
        if calculateHands(computersHand) < 17:
           computersHand.append(dealCard())
           printHands(playersHand, computersHand)

        if(calculateHands(computersHand) > 21):
            print("Player wins!")
            printHands(playersHand, computersHand)
            break
        if calculateHands(computersHand) >= 17:
            if(calculateHands(computersHand) > calculateHands(playersHand) and calculateHands(computersHand) <= 21):
                print("Dealer wins!")
            elif calculateHands(computersHand) == calculateHands(playersHand):
                player_hand_size = len(playersHand)
                computer_hand_size = len(computersHand)
                if(computer_hand_size > player_hand_size):
                    print("Dealer wins!")
                else:
                    print("Player wins!")

            break

playersHand = []
computersHand = []
while True:
    player_hand_size = len(playersHand)
    if(player_hand_size < 1):
        for i in range (2):
            playersHand.append(dealCard())
            computersHand.append(dealCard())

    printHands(playersHand, computersHand)
    if(calculateHands(computersHand) == 21):
        print("Game Over!")
    elif calculateHands(playersHand) == 21:
        print("You win")

    while True:
        playerChoice = input("Do you want to deal?")
        if playerChoice.lower() == 'y':
            playersHand.append(dealCard())
            if(calculateHands(playersHand) > 22):
                printHands(playersHand, computersHand)
                print("Game Over!")
                break
            elif(calculateHands(playersHand) == 21):
                printHands(playersHand, computersHand)
                print("You win!")
                break
            else:
                printHands(playersHand, computersHand)

        else:
            dealerPlay(playersHand, computersHand)
            break
        
    break




