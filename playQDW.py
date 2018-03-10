
import QDW as Game
import time as time


a = Game.QDW(None)
a.display()
a.loadCharacters()

# a.moveZombie(5,1,4,1)
# a.moveZombie(5,2,4,2)

print("******************************")
a.display()


arr=[]



arr=a.findMaxNodePostion(a.gameState)
for i in arr:
    print("The zombies are in the postions (",i[0],",",i[1],")")

print("The queen is at ","(",arr[0][0],",",arr[0][1],")")
for i in arr:
    if i==0:
        continue

    print ("The dragons are at ","(",i[0],",",i[1],")")
arr=a.maxSuccersor()


