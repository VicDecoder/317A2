class QDW:


    def __init__(self,state):
        """
               Create a new object
               :param state: a description of the board for the current state

               :return:
               """

        if state is None:
            self.gameState=dict()
            for row in range(1,6):
                for column in range(1,6):
                    self.gameState[row,column]=' '
        else:
            self.gameState=state

    def str(self):
        """ *** needed for search ***
                Translate the board description into a string.  Could be used as for a hash table...
                :return: A string that describes the board in the current state.
                """
        s=""
        for row in range(1,6):
            for column in range(1,6):
                s += self.gameState[row,column]
        return s
    def display(self):
        """
                A pleasant view of the current game state
                :return: nothing
                """
        for row in range(1, 6):
            print("+-+-+-+-+-+")
            print("|", end="")
            for column in range(1, 5):
                print(self.gameState[row,column], end="")
                print("|",end="")
            print(self.gameState[row,5], end="")
            print("|")
        print("+-+-+-+-+-+")
    def placeCharacter(self,character,row,column):
        """Places a acharacter in a postion on the dictionary"""
        self.gameState[row,column]=character


    def moveQueen(self,destRow,destColumn):
        """Moves the queen the destRow and destColumn"""

        for r in range(1,6):
            for c in range(1,6):
                if self.gameState[r,c]=="Q":
                    self.gameState[r,c]=" "
                    self.gameState[destRow,destColumn]="Q"

    def moveQueen2(self,initRow,initCol,finalRow,finalCol):
        if self.gameState[initRow, initCol] == "Q":
            if self.isMaxMoveValid(initRow, initCol, finalRow, finalCol) and self.checkSides(initRow, initCol, finalRow,
                                                                                             finalCol):
                self.gameState[initRow, initCol] = " "
                self.gameState[finalRow, finalCol] = "Q"

    def moveZombie(self, initRow,initCol,finalRow,finalCol):
        """

        :param initRow: the initail row of the zombie:
        :param initCol: the iniial row of the zombie:
        :param finalRow: the final row of the zombie you want to move:
        :param finalCol: the final column of the package you want to move:
        :Checks if there is a Zombie in that postion
        return:
        """
        if self.gameState[initRow,initCol]=='W':
            if self.isZombieMoveValid(initRow, initCol, finalRow, finalCol) and self.checkSides(initRow,initCol, finalRow, finalCol):
                self.gameState[initRow, initCol] = ' '
                self.gameState[finalRow, finalCol] = 'W'


    def moveDragon(self, initRow, initCol, finalRow, finalCol):
        """

        :param initRow: the initail row of the dragon:
        :param initCol: the iniial row of the dragon:
        :param finalRow: the final row of the dragon you want to move:
        :param finalCol: the final column of the dragon you want to move:
        :Checks if there is a dragon in that postion
        return:
        """
        if self.gameState[initRow, initCol] == "D":
           if self.isMaxMoveValid(initRow,initCol,finalRow,finalCol) and self.checkSides(initRow,initCol, finalRow, finalCol):
            self.gameState[initRow, initCol] = " "
            self.gameState[finalRow, finalCol] = "D"

    def loadCharacters(self):
        """
              A pleasant view of the current game state
                :return: nothing
                 """
        queen="Q"
        dragons="D"
        zombie="W"
        self.placeCharacter(queen,1,3)
        self.placeCharacter(dragons,2,2)
        self.placeCharacter(dragons, 2, 3)
        self.placeCharacter(dragons, 2, 4)
        self.placeCharacter(zombie, 5, 1)
        self.placeCharacter(zombie, 5, 2)
        self.placeCharacter(zombie, 5, 3)
        self.placeCharacter(zombie, 5, 4)
        self.placeCharacter(zombie, 5, 5)


    def checkSides(self,initR,initCol,finalR,finalC):
        if initCol==1 and finalC <1:
            return False
        if initR==1 and finalR <1:
            return False
        if initR==5 and finalR >5:
            return False
        if initCol==5 and finalC >5:
            return False
        if abs(finalR-initR) == 1 or abs(finalC - initCol) == 1:
            return True
        else:
            return False


    def isZombieMoveValid(self,initR,initCol,finalR,finalC):
        """

        :param initR: THe initial row of the zombie
        :param initCol: The initial colums of the zombie
        :param finalR: The final row of the zombie
        :param finalC:the final column of th zombie
        :return: true is the moves is valid
        """

        if self.checkSides(initR,initCol,finalR,finalC) and (self.gameState[finalR,finalC]=='D' or self.gameState[finalR,finalC]== 'Q'):
            print("The value is either q or d")
            return True

        if self.checkSides(initR, initCol, finalR, finalC) and self.gameState[finalR, finalC] == 'W':
            print("The value is W")
            return False
        return True

    def isMaxMoveValid(self,initR,initCol,finalR,finalC):
        if self.checkSides(initR, initCol, finalR, finalC) and self.gameState[finalR, finalC] == 'D':
            return False
        return True









