import QDW as Game
from MinMax import minimax
from MinMax import alphaBeta
import time as time

print("Welcome to the game")
a=Game.QDW(None)
a.loadCharacters()
iR=0
itC=0
fC=0
fR=0
a.display()
while not a.isTerminal():
    print("TYPE \"MOVE the initital postion anf final\(MOVE 1,5-1,4)\" to make the character go  ")
    value=input("Enter the positon:")
    iR=int(value[5:6])
    iC=int(value[7:8])
    fR=int(value[9:10])
    fC=int(value[11:12])
    if a.isZombieMoveValid(iR,iC,fR,fC):
        a.moveZombie(iR,iC,fR,fC)
        a.display()
        a.whoseTurn='MAX'
        result = alphaBeta(a, 3)
        a=result
        print("******************************************")
        a.display()
    else:
        print("Invalid Move")
        a.display()
