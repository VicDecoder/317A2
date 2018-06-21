# 317A2
AI Assignment 2

The Dragon Queen
The Dragon Queen is a game played on a board with 5 columns and 5 rows. One player (Player 1) controls the Queen, who has three Dragon protectors.  The other player (Player 2) controls 5 wights (a.k.a zombies).  (This game, as far as I know, is a completely unique invention; I don't think you'll find anything quite like it anywhere, which is the whole point).  

The Dragon Queen could be a Mad King, with a King's Guard.  Or the Wights could be Daleks.  Or the Wights could be Sith-Lords, with the Queen as a Fleeing Senator, guarded by Jedi Protectors.  

Initial Position

The initial position is as follows.  
  
. . Q . .  
. D D D .   
. . . . .  
. . . . .  
W W W W W  
Traditionally, the Wights move first (Player 2).  
End of Game. 

Win for Player 1: the Queen reaches the Wight's home row (the bottom of the board in the above diagram).  
Win for Player 2: the Queen is captured.    
Draw:  
One player cannot move.
No win for either player after 50 ply (25 complete turns).  
Movement of pieces:  

Wights can move forward, backward, left, or right, by one square if it is not occupied, but not diagonally.  
(wights' movement is somewhat similar to pawns in Chess). 
The Queen and the Dragons can move to any adjacent empty square, vertically, horizontally, or diagonally.  
(the Queen's and the dragons' movement is similar to the king in Chess). 
Capture:  

A Wight can capture by moving diagonally (in any diagonal direction) into the square occupied by an opposing piece (a Dragon or the Queen).  
(wights' capture is somewhat similar to pawns in chess)
A Dragon or the Queen can capture by normal movement into a square occupied by a Wight.  
(Dragons' and Queen's capture is similar to the king in Chess)
Capture is not forced. 
Other rules:  

A player must move if a move is possible.  



External Libraries. 
import sys  
import time  

To run the code in terminal, go to file HumanVsAI.py and run it
To run the gui , open the file ManVsAI(GUI).py  and click run.
When running the gui click on the initial position and then the final position don't click on anywhere else on the board
