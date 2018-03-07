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

