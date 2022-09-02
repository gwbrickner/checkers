# Graeson Brickner
# Checkers
# poop code :)

#i have no idea how any of this is functioning so don't ask me

#to do list
#2. finish implementing the kinging system along with how it starts
#3. implement the win system
#4. weep at my new creation

#ignore the sqigglies i cant make them leave its stupid and i dont like it

from logic import *


print(printCheckerBoard(getPositionOfCheckers()))

while True:
  tmialo()
  print(printCheckerBoard(getPositionOfCheckers()))
  
  tmialx()
  print(printCheckerBoard(getPositionOfCheckers()))
  
  if 1 in positionOfCheckers:
    print("1 is still there")

  if 2 in positionOfCheckers:
    print("2 is still there")