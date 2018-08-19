

##############class#####################
class Board:
    """ This class defines the board object used in the game"""

##############constructeur##################
    def __init__(self):
        self.boardTab = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.boardDic = {"A1":[0,"A2"],"A2":[0,"A3"],"A3":[0,"A4"],"A4":[0,"C1"],"A5":[0,"A6"],"A6":[0,"Safe"],"B5":[0,"B6"],"B6":[0,"Safe"],"B1":[0,"B2"],"B2":[0,"B3"],"B3":[0,"B4"],"B4":[0,"C1"],"C1":[0,"C2"],"C2":[0,"C3"],"C3":[0,"C4"],"C4":[0,"C5"],"C5":[0,"C6"],"C6":[0,"C7"],"C7":[0,"C8"],"C8":[0,["B5","A5"]]}

    def show(self):
        print("""P1 : [A1: %s][A2: %s][A3: %s][A4: %s]             [A5: %s][A6: %s] \n     [C1: %s][C2: %s][C3: %s][C4: %s][C5: %s][C6: %s][C7: %s][C8: %s] \nP2 : [B1: %s][B2: %s][B3: %s][B4: %s]             [B5: %s][B6: %s]
         """ % (self.boardDic["A1"][0],self.boardDic["A2"][0],self.boardDic["A3"][0],self.boardDic["A4"][0],self.boardDic["A5"][0],self.boardDic["A6"][0],self.boardDic["C1"][0],self.boardDic["C2"][0],self.boardDic["C3"][0],self.boardDic["C4"][0],self.boardDic["C5"][0],self.boardDic["C6"][0],self.boardDic["C7"][0],self.boardDic["C8"][0],self.boardDic["B1"][0],self.boardDic["B2"][0],self.boardDic["B3"][0],self.boardDic["B4"][0],self.boardDic["B5"][0],self.boardDic["B6"][0]))
