
import QDW as Game
import time as time


a = Game.QDW(None)
a.display()
a.loadCharacters()
print("******************************")
a.display()
arr=[]

arr=a.findMinNodePostion()
for i in arr:
    print("The zombies are in the postions (",i[0],",",i[1],")")
arr=a.findMaxNodePostions()

print("The queen is at ","(",arr[0][0],",",arr[0][1],")")
for i in arr:
    if i==0:
        continue

    print ("The dragons are at ","(",i[0],",",i[1],")")
arr=a.minSuccersor()
for i in arr:
    print("************************")
    print(i)

