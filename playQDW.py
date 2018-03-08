
import QDW as Game
import time as time


a = Game.QDW(None)
a.display()
a.loadCharacters()
print("******************************")
a.display()
a.moveQueen(1,2)
print("******************************")
a.display()
a.moveZombie(5,1,4,1)
print("******************************")
a.display()
a.moveDragon(2,2,3,2)
print("******************************")
a.display()
a.moveZombie(4,1,4,0)
print("******************************")
a.display()
