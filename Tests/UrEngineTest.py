from Objects.Board import *
from Engine.UrEngine import *
import unittest

game=UrEngine()
#game.printGame()

class TestUrEngineMethods(unittest.TestCase):


    #game.printGame()

    def testUREngine_AddPawn(self):
        game1 = UrEngine()
        self.assertEqual(game1.playerAddPawn(1,1),"MoveOK")
        self.assertEqual(game1.playerAddPawn(2,2),"MoveOK")
        #game.printGame()

    def testUrEngine_scopeThroughBoard(self):
        game2 = UrEngine()
        game2.board.placePawn(1,"A2")
        game2.board.placePawn(2, "B3")
        game2.board.placePawn(2, "C1")
        game2.board.placePawn(1, "C2")

        self.assertEqual(game2.scopeThroughBoard(4,"forward","A2",1),["MoveKO",""])
        self.assertEqual(game2.scopeThroughBoard(3,"forward","B1",2),['MoveOKReplay', 'B4'])
        self.assertEqual(game2.scopeThroughBoard(3, "forward", "A2", 1), ['MoveReplace', 'C1'])
        self.assertEqual(game2.scopeThroughBoard(2, "forward", "C7", 2), ['MoveOK', 'B5'])
        self.assertEqual(game2.scopeThroughBoard(2, "forward", "C7", 1), ['MoveOK', 'A5'])
        self.assertEqual(game2.scopeThroughBoard(2,"backward", "B6",2),['MoveOK','C8'])
        self.assertEqual(game2.scopeThroughBoard(2, "forward", "B5", 2), ['PawnSafe', ''])


        # self.assertEqual(game2.scopeThroughBoard(4, "forward", "A5", 1), ['MoveOK', 'A5'])
    def testUrEngine_movePlayerPawn(self):
        game3 = UrEngine()
        game3.board.placePawn(1,"A2")
        self.assertEqual(game3.movePlayerPawn(3,"A2",1),"MoveOK")
        self.assertEqual(game3.board.getSquareState("C1"),1)
        self.assertEqual(game3.movePlayerPawn(3, "A3", 1), "MoveKO")








if __name__ == '__main__':
    unittest.main()
