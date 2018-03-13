import QDW as Game
from MinMax import minimax
from MinMax import alphaBeta
import time as time
from tkinter import *
import tkinter


root = tkinter.Tk()
# Code to add widgets will go here...
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create a 5x10 (rows x columns) grid of buttons inside the frame

def stateToButton(state,temp):
    for r in range(1,6):
        for c in range(1,6):
            temp[r,c]['text']=state[r,c]

temp=dict()
for row_index in range(1,6):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(1,6):
        Grid.columnconfigure(frame, col_index, weight=1)
        btn = Button(frame, command= lambda row=row_index, col=col_index: buttonClick(row, col)) #create a button inside frame
        btn['text']= ' '
        temp[row_index, col_index]=btn
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)

print("Welcome to the game")
a=Game.QDW(None)
a.loadCharacters()
stateToButton(a.gameState,temp)
r=None
c=None
R=None
C=None

def buttonClick(row,col):
    global r
    global c
    global R
    global C

    if  r==None:
        r=row
    else:
        R=row
    if c==None:
        c=col
    else:
        C=col
    if r!=None and c!=None and R!= None and  C!= None:
        if a.isZombieMoveValid(r,c,R,C):
            a.moveZombie(r,c,R,C)
            r=None
            c=None
            R = None
            C = None
            stateToButton(a.gameState, temp)
            AiMove()

            print("Here")
        else:
            L=Label(frame, text="You win")
            r = None
            c = None
            R = None
            C = None
def AiMove():
    global  a

    a.whoseTurn='MAX'
    result = alphaBeta(a, 3)
    a = result
    stateToButton(a.gameState, temp)












root.mainloop()