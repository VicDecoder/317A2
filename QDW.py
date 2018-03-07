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