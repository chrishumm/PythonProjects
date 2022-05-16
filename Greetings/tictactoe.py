the_board = {'A1': 'A1', 'A2': 'A2', 'A3': 'A3',
            'B1': 'B1', 'B2': 'B2', 'B3': 'B3',
            'C1': 'C1', 'C2': 'C2', 'C3': 'C3'}

def printBoard(the_board):
    printBoard = 0
    while printBoard < 3:
        if printBoard ==0 :
            for i in range(1,4):
                print('|' + the_board['A' +str(i)] + '|  ', end='')
            printBoard +=1

        elif printBoard == 1:
            for i in range(1,4):
                print('|' + the_board['B' +str(i)] + '|  ', end='')
            printBoard+=1
        else:
            for i in range(1,4):
                print('|' + the_board['C' +str(i)] + '|  ', end='')
            printBoard+=1
        
        print()

def checkWin(the_board, turn):
## Horizontal
    if (the_board['A1'] == turn and the_board['A2'] == turn and
            the_board['A3'] == turn)  or (the_board['B1'] == turn and
            the_board['B2'] == turn and the_board['B3'] == turn) or (the_board['C1'] == turn 
            and the_board['C2'] == turn and the_board['C3'] == turn):
                print(turn +  ' wins')
                return True

## Column
    the_same = 0
    for x in range(1,4):
       if (the_board['A' +str(x)] == turn and
         the_board['B' +str(x)] == turn and 
         the_board['C' +str(x)] == turn):
            print(turn +  ' wins')
            return True

## Check diagnonal
    if(the_board['A1'] == turn and the_board['B2'] == turn
        and the_board ['C3'] == turn) or (the_board['A3'] == turn
        and the_board['B2'] == turn and the_board['C1'] == turn):
        print(turn +  ' wins')
        return True

for i in range(9):
    printBoard(the_board)
    if(i % 2 == 0):
        turn = 'X'
    else:
        turn = 'O'
    print(turn +"'s turn, please enter your move:")
    while True:
            move = input().upper()
            if move not in the_board.keys() or the_board[move] == 'X' or the_board[move] == 'O':
                print("Please enter a valid move")
                printBoard(the_board)
            else:
                break


    the_board[move] = turn
    if i >= 4:
         if checkWin(the_board, turn) == True:
             break
         elif i >= 8:
            print("It's a tie!")
            break

