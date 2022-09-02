
import numpy as np

positionOfCheckers = np.array([
    [0, 0, 0, 2, 0, 2, 0, 2],
    [2, 0, 1, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]])

pieceDict = {
  0:"   ",
  1:" o ",
  2:" x ",
  3:" O ",
  4:" X "
}
# prints current checkerboard and returns the "checkerboard string", a parsed version of the array that constructs the checkerboard

def printCheckerBoard(position_of_checkers):
    posArrayX = 0
    posArrayY = 0
    checkerBoard = '  0  1  2  3  4  5  6  7\n0'

    #loops through all of the squares
    for x in range(64):

      #obtains number at current pointer position
        currentPiece = position_of_checkers[posArrayY, posArrayX]

        checkerBoard = checkerBoard + pieceDict.get(currentPiece, "   ")

        #if we have reached the end of the line then we should move to the next line
          
        if posArrayX == 7:
            posArrayX = 0
            posArrayY += 1
            checkerBoard = checkerBoard + '\n' + str(posArrayY)
          
        #else increment the x position counter
        else:
            posArrayX += 1

    return checkerBoard

#way too scuffed
def getPositionOfCheckers():
  return positionOfCheckers

# updates the piece position, arguments are self explanatory
def updatePieceReg(movePieceX, movePieceY, movePlaceX, movePlaceY, pieceType):

  positionOfCheckers[movePieceY, movePieceX] = 0
  positionOfCheckers[movePlaceY, movePlaceX] = pieceType

#piece position update is a piece is being captured
def updatePieceCap(movePieceX, movePieceY, movePlaceX, movePlaceY, pieceType, directionX, directionY):

  positionOfCheckers[movePieceY, movePieceX] = 0
  positionOfCheckers[movePlaceY, movePlaceX] = 0
  positionOfCheckers[movePlaceY + directionY, movePlaceX + directionX] = pieceType
  
# take move input and logic x
def tmialo():
    # input logic, to be made into function
    movePieceX = int(input('Input X Value of Piece'))
    movePieceY = int(input('Input Y Value of Piece'))
    movePlaceX = int(input('Input X Value of Destination'))
    movePlaceY = int(input('Input Y Value of Destination'))
  
    # if piece is on square selected
    if positionOfCheckers[movePieceY, movePieceX] == 1:

        # if target square is empty
        if positionOfCheckers[movePlaceY, movePlaceX] == 0:

            # making sure that you are moving up and left
            if movePieceX - movePlaceX == 1 & movePieceY - movePlaceY == 1:

                updatePieceReg(movePieceX, movePieceY, movePlaceX, movePlaceY, 1)

            # making sure that you are moving up and right
            elif movePlaceX - movePieceX == 1 & movePieceY - movePlaceY == 1:

                updatePieceReg(movePieceX, movePieceY, movePlaceX, movePlaceY, 1)

        # else if the target piece is holding an enemy piece
        elif positionOfCheckers[movePlaceY, movePlaceX] == 2:

            # making sure its moving in a legal direction, up and left
            if movePieceX - movePlaceX == 1 & movePieceY - movePlaceY == 1 & positionOfCheckers[movePlaceY - 1, movePlaceX - 1] == 0:
                  
              updatePieceCap(movePieceX, movePieceY, movePlaceX, movePlaceY, 1, -1, -1)

            # making sure its moving in a legal direction, up and right
            elif movePlaceX - movePieceX == 1 & movePieceY - movePlaceY == 1 & positionOfCheckers[movePlaceY - 1, movePlaceX + 1] == 0:
                
              updatePieceCap(movePieceX, movePieceY, movePlaceX, movePlaceY, 1, 1, -1)

    else:
      print("Invalid square, please retry.")
      tmialo()
    checkForKing(movePlaceX, movePlaceY, 3)
    return positionOfCheckers

# take input and logic "x"
def tmialx():
  #
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

                updatePieceReg(movePieceX, movePieceY, movePlaceX, movePlaceY, 2)

            # making sure that you are moving down and right
            elif movePlaceX - movePieceX == 1 & movePlaceY - movePieceY == 1:

                updatePieceReg(movePieceX, movePieceY, movePlaceX, movePlaceY, 2)

        # else if the target piece is holding an enemy piece
        elif positionOfCheckers[movePlaceY, movePlaceX] == 1 or positionOfCheckers[movePlaceY, movePlaceX] == 3:

            # making sure its moving in a legal direction
            if movePieceX - movePlaceX == 1 & movePlaceY - movePieceY == 1 & positionOfCheckers[movePlaceY + 1, movePlaceX - 1] == 0:

              updatePieceCap(movePieceX, movePieceY, movePlaceX, movePlaceY, 2, -1, 1)

            elif movePlaceX - movePieceX == 1 & movePlaceY - movePieceY == 1 & positionOfCheckers[movePlaceY + 1, movePlaceX + 1] == 0:

              updatePieceCap(movePieceX, movePieceY, movePlaceX, movePlaceY, 2, 1, 1)
              
    #if the piece is a king
    elif positionOfCheckers[movePieceY, movePieceX] == 4:
      
      #no matter what direction if its legal it can move
      if positionOfCheckers[movePlaceY, movePlaceX] == 0:
        
        kingLogicReg(movePieceX, movePieceY, movePlaceX, movePlaceY, 4)
      #if enemy piece, i hate this code so bad
      elif positionOfCheckers[movePlaceY, movePlaceX] == 1:
        
        movementDirX = movePlaceX - movePieceX
        movementDirY = movePlaceY - movePieceY
        updatePieceCap(movePieceX, movePieceY, movePlaceX, movePlaceY, 4, movementDirX, movementDirY)

        
    else:
      print("Invalid square, please retry.")
      tmialx()
    checkForKing(movePlaceX, movePlaceY, 4)
    return positionOfCheckers


def kingLogicReg(movePieceX, movePieceY, movePlaceX, movePlaceY, pieceType):
  if movePieceX - movePlaceX == 1 & movePlaceY - movePieceY == 1 or movePlaceX - movePieceX == 1 & movePieceY - movePlaceY == 1 or movePlaceX - movePieceX == 1 & movePlaceY - movePieceY == 1 or movePlaceX - movePieceX == 1 & movePieceY - movePlaceY == 1:
    updatePieceReg(movePieceX, movePieceY, movePlaceX, movePlaceY, pieceType)

def checkForKing(movePlaceX, movePlaceY, pieceType):
  if pieceType == 1:
    if positionOfCheckers[movePlaceY] == 0:
      positionOfCheckers[movePlaceY, movePlaceX] == 3
    
  if pieceType == 2:
    if positionOfCheckers[movePlaceY] == 7:
      positionOfCheckers[movePlaceY, movePlaceX] == 4
