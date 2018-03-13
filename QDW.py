from random import randint
class QDW:


    def __init__(self,state,player='MIN'):
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
            self.gameState = state
        self.whoseTurn = player


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
        if abs(finalR - initR) == 1 and abs(finalC - initCol) == 0:

            return True
        if abs(finalR - initR) == 1 and abs(finalC - initCol) == 1:

            return True
        if abs(finalR - initR) == 0 and abs(finalC - initCol) == 1:

            return True

        if initCol==1 and finalC <1:

            return False
        if initR==1 and finalR <1:

            return False
        if initR==5 and finalR >5:

            return False
        if initCol==5 and finalC >5:

            return False


        # if abs(finalC - initCol) == 1:
        #     return True
        else:
            return False
        return True




    def isZombieMoveValid(self,initR,initCol,finalR,finalC):
        """

        :param initR: THe initial row of the zombie
        :param initCol: The initial colums of the zombie
        :param finalR: The final row of the zombie
        :param finalC:the final column of th zombie
        :return: true is the moves is valid
        """
        if self.checkSides(initR,initCol,finalR,finalC):

            if(self.gameState[finalR,finalC]=='D' or self.gameState[finalR,finalC]== 'Q') and self.isDiagonal(initR,initCol,finalR,finalC):

                return True

            if self.gameState[finalR, finalC] == 'W':

                return False
            if self.gameState[finalR,finalC] == " "  and self.isDiagonal(initR,initCol,finalR,finalC):

                return False
            if (self.gameState[finalR,finalC] == 'Q'or self.gameState[ finalR , finalC] == 'D') and (not self.isDiagonal(initR,initCol,finalR,finalC)):

                return False
            # if not self.checkSides(initR, initCol, finalR, finalC):
            #     print("It checks if they are equal")
            #     return False
            """
            I added a statement here to make sure a player can not make a move on itself
            """
            if initR==finalR and initCol==finalC:

                return False
            if self.gameState[initR,initCol] == ' ':

                return False
        return True

    def isMaxMoveValid(self,initR,initCol,finalR,finalC):
        if self.checkSides(initR, initCol, finalR, finalC) and self.gameState[finalR, finalC] == 'D' or self.gameState[finalR, finalC] == 'Q':
            return False
        return True
    def isDiagonal(self, initR,initC,finalR,finalC):
        if((finalR-initR) == 1 and (finalC-initC) == 1):
            return True
        if ((finalR - initR) == 1 and (finalC - initC) == -1):
            return True
        if ((finalR - initR) == -1 and (finalC - initC) == 1):
            return True
        if ((finalR - initR) == -1 and (finalC - initC) == -1):
            return True
        else:
            return False
    def findMinNodePostion(self,state):
        array = []

        for r in range(1, 6):
            for c in range(1, 6):
                if state[r, c] == 'W':
                    tup = (r, c)
                    array.append(tup)
        return array

    def findMaxNodePostion(self,state):
        """

        :return: This function return as array of tuple containing
        """
        array = []

        for r in range(1, 6):
            for c in range(1, 6):
                if state[r, c] == 'D':
                    tup = (r, c)
                    array.append(tup)

        for r in range(1, 6):
            for c in range(1, 6):
                if state[r, c] == 'Q':
                    tup = (r, c)
                    array.insert(0, tup)
        return array
    def copyState(self,state):
        returnState=dict()
        for r in range(1,6):
            for c in range(1,6):
                returnState[r,c]=state[r,c]
        return returnState
    def moveMax(self,initR,initCol,finalR,finalC):
        self.moveQueen2(initR,initCol,finalR,finalC)
        self.moveDragon(initR,initCol,finalR,finalC)

    def minSuccersor(self):
        states = []
        orginalState = self.copyState(self.gameState)
        temp = self.findMinNodePostion(orginalState)
        for i in temp:
            self.gameState = self.copyState(orginalState)
            for r in range(1, 6):
                self.gameState = self.copyState(orginalState)
                for c in range(1, 6):
                    self.gameState = self.copyState(orginalState)
                    if self.isZombieMoveValid(i[0], i[1], r, c) and self.checkSides(i[0], i[1], r, c):
                        self.gameState = self.copyState(orginalState)

                        self.moveZombie(i[0], i[1], r, c)

                        states.append(QDW(self.gameState,'MAX'))

        self.gameState = self.copyState(orginalState)

        return states

    def maxSuccersor(self):
        states = []
        orginalState = self.copyState(self.gameState)
        temp = self.findMaxNodePostion(orginalState)
        for i in temp:
            self.gameState = self.copyState(orginalState)
            for r in range(1, 6):
                self.gameState = self.copyState(orginalState)
                for c in range(1, 6):
                    self.gameState = self.copyState(orginalState)
                    if self.isMaxMoveValid(i[0], i[1], r, c) and self.checkSides(i[0], i[1], r, c):
                        self.gameState = self.copyState(orginalState)
                        self.moveMax(i[0], i[1], r, c)

                        states.append(QDW(self.gameState,'MIN'))
        self.gameState = self.copyState(orginalState)

        return states

    def winFor(self,temp):
        if temp=='MAX':
            value =True
            for r in range(1,6):
                for c in range(1,6):
                    if r==5 and self.gameState[r,c]=='Q':
                        value= True
                    if self.gameState[r,c]=='W':
                        value=False
            return value
        if temp =='MIN':
            value=True
            for r in range(1,6):
                for c in range(1,6):
                    if self.gameState[r,c]=='Q':
                        value=False
            return value


    def isTerminal(self):
        """ *** needed for search ***
        :param node: a game tree node with stored game state
        :return: a boolean indicating if node is terminal
        """
        return self.winFor('MAX') or self.winFor('MIN') #or (len(self.allBlanks()) == 0) #Change this later to check if its a terminal

    def togglePlayer(self,player):
        if player=='MAX':

            self.whoseTurn= 'MIN'
        if player == 'MIN':

            self.whoseTurn= 'MAX'



    def isMinNode(self):
        """ *** needed for search ***
        :return: True if it's Min's turn to play
        """
        return self.whoseTurn == 'MAX'


    def isMaxNode(self):
        """ *** needed for search ***
        :return: True if it's Max's turn to play
        """
        return self.whoseTurn == 'MIN'


    def successors(self):
        if self.whoseTurn=='MAX':
            #self.togglePlayer('MAX')

            return self.maxSuccersor()
        else:

            #self.togglePlayer('MIN')

            return self.minSuccersor()

    def utility(self):
        """ *** needed for search ***
        :return: 1 if win for X, -1 for win for O, 0 for draw
        """
        if self.winFor('MAX'):
            return 1
        elif self.winFor('MIN'):
            return -1
        else:
            return randint(-50,50)