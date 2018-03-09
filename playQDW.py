
import QDW as Game
import time as time


a = Game.QDW(None)
a.display()
a.loadCharacters()
print("******************************")
a.display()
a.moveQueen(1, 2)
a.display()
print("******************************")
a.moveZombie(5,1,4,1)
print("******************************")
a.display()
a.moveZombie(4,1,3,1)
print("******************************")
a.display()
a.moveZombie(3,1,2,2)
print("******************************")
a.display()
a.moveZombie(2,2,1,2)
print("******************************")
a.display()
array =a.findZombies()
tup=()
# for i in array:
#     tup=array.pop(i)

print (str(array)[1:-1])




# print(a.isDiagonal(2,2,1,2))
# a.display()
# a.moveZombie(5, 1, 4, 1)
# print("******************************")
# a.display()
# a.moveDragon(2, 2, 3, 2)
# print("******************************")
# a.display()
# a.moveZombie(4, 1, 4, 0)
# print("******************************")
# a.display()
# a.moveZombie(5, 5, 4, 5)
# print("******************************")
# a.display()
# a.moveZombie(5, 3, 4, 5)
# print("******************************")
# a.display()
# a.moveZombie(4,1,4,3)
# print("******************************")
# a.display()
# a.moveQueen2(1,2,2,3)
# print("******************************")
# a.display()
