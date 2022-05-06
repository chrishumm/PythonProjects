import random
wins = 0
losses = 0
ties = 0
playerMove = ""
computerMove = ""


class player:
  def __init__(self, wins, losses, ties):
    self.wins = 0
    self.losses = 0
    self.ties = 0
    
playerOne = player(0,0,0)
    
def win_game(wins):
    print("You win! Congratulations")
    playerOne.wins += 1

def lose_game(losses):
    print("You lose! Try again!")
    playerOne.losses +=1
def tie_game(ties):
    print("Its a tie!")
    playerOne.ties +=1
    
def calcComputerMove():
    compMove = random.randint(1,3)
    if compMove == 1:
        return "PAPER"
    elif compMove == 2:
        return "SCISSORS"
    elif compMove == 3:
        return "ROCK"
    
    return ""

def calcResult():
    if (playerMove == "s" or playerMove == "S") and computerMove == "SCISSORS":
        tie_game(ties)
        return True
    elif (playerMove == "s" or playerMove == "S") and computerMove == "ROCK":
        lose_game(losses)
        return True
    elif(playerMove == "s" or playerMove == "S") and computerMove == "PAPER":
        win_game(wins)
        return True
    elif (playerMove == "r" or playerMove == "R") and computerMove == "ROCK":
        tie_game(ties)
        return True
    elif(playerMove == "r" or playerMove == "R") and computerMove == "PAPER":
        lose_game(losses)
        return True
    elif(playerMove == "r" or playerMove == "R") and computerMove == "SCISSORS":
        win_game(wins)
        return True
    elif (playerMove == "p" or playerMove == "P") and computerMove == "ROCK":
        win_game(wins)
        return True
    elif(playerMove == "p" or playerMove == "P") and computerMove == "PAPER":
        tie_game(ties)
        return True
    elif(playerMove == "p" or playerMove == "P") and computerMove == "SCISSORS":
        lose_game(losses)
        return True
    else:
        print("Choose a valid move!")
        return False

#Main game loop
while True:
    
    print("You have "+ str(playerOne.wins)+" wins, " + str(playerOne.losses) +" losses and " + str(playerOne.ties) + " ties.")
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")

    playerMove = input()
    computerMove = calcComputerMove()
    
    if playerMove == "q" or playerMove == "Q":
        break
    elif playerMove == "s" or playerMove == "S":
        print("SCISSORS VS "+ computerMove)
    elif playerMove == "r" or playerMove =="R":
        print("ROCK VS " + computerMove)
    elif playerMove == "p" or playerMove == "P":
        print ("PAPER VS "+ computerMove)
        
    calcResult()
