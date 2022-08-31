import numpy as np

# initial board state
positionOfCheckers = np.array([
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]])


# prints current checkerboard

def printCheckerBoard(position_of_checkers):
    posArrayX = 0
    posArrayY = 0
    checkerBoard = ''

    for x in range(64):

        currentPiece = position_of_checkers[posArrayY, posArrayX]

        if currentPiece == 1:
            checkerBoard = checkerBoard + " O "

        elif currentPiece == 2:
            checkerBoard = checkerBoard + " o "

        else:
            checkerBoard = checkerBoard + "   "

        if posArrayX == 7:
            posArrayX = 0
            posArrayY += 1
            checkerBoard = checkerBoard + '\n'

        else:
            posArrayX += 1

    return checkerBoard


# take move input and logic uppercase
def tmialu():
    movePieceX = int(input('Input X Value of Piece'))
    movePieceY = int(input('Input Y Value of Piece'))
    movePlaceX = int(input('Input X Value of Destination'))
    movePlaceY = int(input('Input Y Value of Destination'))

    #if piece is on square
    if positionOfCheckers[movePieceY, movePieceX] == 1:

        #if target square is empty
        if positionOfCheckers[movePlaceY, movePlaceX] == 0:

            #making sure that you are moving up and left
            if movePieceX - movePlaceX == 1 & movePieceY - movePlaceY == 1:

                print('cond satisfied')
                positionOfCheckers[movePieceY, movePieceX] = 0
                positionOfCheckers[movePlaceY, movePlaceX] = 1

            #making sure that you are moving up and right
            elif movePlaceX - movePieceX == 1 & movePieceY - movePlaceY == 1:

                print('cond satisfied')
                positionOfCheckers[movePieceY, movePieceX] = 0
                positionOfCheckers[movePlaceY, movePlaceX] = 1

            else:
                print('error thrown, invalid move')

        #else if the target piece is holding an enemy piece
        elif positionOfCheckers[movePlaceY, movePlaceX] == 2:

            #making sure its moving in a legal direction, up and left
            if movePieceX - movePlaceX == 1 & movePieceY - movePlaceY == 1:
                if positionOfCheckers[movePlaceY - 1, movePlaceX - 1] == 0:
                    print('cond satisfied')
                    positionOfCheckers[movePieceY, movePieceX] = 0
                    positionOfCheckers[movePlaceY, movePlaceX] = 0
                    positionOfCheckers[movePlaceY - 1, movePlaceX - 1] = 1

             # making sure its moving in a legal direction, up and right
            elif movePlaceX - movePieceX == 1 & movePieceY - movePlaceY == 1:
                if positionOfCheckers[movePlaceY - 1, movePlaceX + 1] == 0:
                    print('cond satisfied')
                    positionOfCheckers[movePieceY, movePieceX] = 0
                    positionOfCheckers[movePlaceY, movePlaceX] = 0
                    positionOfCheckers[movePlaceY - 1, movePlaceX + 1] = 1
        else:
            print('error thrown, invalid move')

        return positionOfCheckers
    else:
        print('error thrown, invalid move')


# take input and logic lowercase
def tmiall():
    movePieceX = int(input('Input X Value of Piece'))
    movePieceY = int(input('Input Y Value of Piece'))
    movePlaceX = int(input('Input X Value of Destination'))
    movePlaceY = int(input('Input Y Value of Destination'))

    # if piece is on square
    if positionOfCheckers[movePieceY, movePieceX] == 2:

        # if target square is empty
        if positionOfCheckers[movePlaceY, movePlaceX] == 0:

            # making sure that you are moving down and left
            if movePieceX - movePlaceX == 1 & movePlaceY - movePieceY == 1:

                print('cond satisfied')
                positionOfCheckers[movePieceY, movePieceX] = 0
                positionOfCheckers[movePlaceY, movePlaceX] = 2

            # making sure that you are moving down and right
            elif movePlaceX - movePieceX == 1 & movePlaceY - movePieceY == 1:

                print('cond satisfied')
                positionOfCheckers[movePieceY, movePieceX] = 0
                positionOfCheckers[movePlaceY, movePlaceX] = 2

            else:
                print('error thrown, invalid move step 3')

        # else if the target piece is holding an enemy piece
        elif positionOfCheckers[movePlaceY, movePlaceX] == 1:

            # making sure its moving in a legal direction, up and left
            if movePieceX - movePlaceX == 1 & movePlaceY - movePieceY == 1:

                if positionOfCheckers[movePlaceY + 1, movePlaceX - 1] == 0:
                    print('cond satisfied')
                    positionOfCheckers[movePieceY, movePieceX] = 0
                    positionOfCheckers[movePlaceY, movePlaceX] = 0
                    positionOfCheckers[movePlaceY + 1, movePlaceX - 1] = 2

            # making sure its moving in a legal direction, up and right
            elif movePlaceX - movePieceX == 1 & movePlaceY - movePieceY == 1:

                if positionOfCheckers[movePlaceY + 1, movePlaceX + 1] == 0:
                    print('cond satisfied')
                    positionOfCheckers[movePieceY, movePieceX] = 0
                    positionOfCheckers[movePlaceY, movePlaceX] = 0
                    positionOfCheckers[movePlaceY + 1, movePlaceX + 1] = 2

        else:
            print('error thrown, invalid move step 2')

        return positionOfCheckers
    else:
        print('error thrown, invalid move step 1')


print(printCheckerBoard(positionOfCheckers))
tmialu()
print(printCheckerBoard(positionOfCheckers))
tmiall()
print(printCheckerBoard(positionOfCheckers))
tmialu()
print(printCheckerBoard(positionOfCheckers))
tmiall()
print(printCheckerBoard(positionOfCheckers))