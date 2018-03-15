
import QDW as Game
from MinMax import minimax
from MinMax import alphaBeta
import time as time

a = Game.QDW(None)
a.loadCharacters()
a.display()
print("THe gmae size ",a.getSize())



# a.maxSuccersor()

i = 0

while (not a.isTerminal()) and i < 50:
    start = time.process_time()
    result = minimax(a)
    end = time.process_time()
    print('Took', end-start, 'seconds to determine the minimax value', result[0])
    result[1].display()
    a = result[1]
    print(i)
    i= i + 1



# while (not a.isTerminal() ) and i < 50:
#     start = time.process_time()
#     result = alphaBeta(a,3)
#     end = time.process_time()
#     print('Took', end-start, 'seconds to determine the minimax value')
#
#     result.display()
#     a=result
#     i= i + 1
