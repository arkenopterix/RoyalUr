from Objects.Board import *
from Engine.UrEngine import *
import unittest

game=UrEngine()
#game.printGame()

class TestUrEngineMethods(unittest.TestCase):


    #game.printGame()

    def testUREngine_AddPawn(self):
        game1 = UrEngine()
        self.assertTrue(game1.playerAddPawn(1,1))
        self.assertTrue(game1.playerAddPawn(2,2))
        #game.printGame()

    def testUrEngine_scopeThroughBoard(self):
        game2 = UrEngine()
        game2.board.placePawn(1,"A2")
        game2.board.placePawn(2, "B3")
        game2.board.placePawn(2, "C1")
        game2.board.placePawn(1, "C2")
        self.assertEqual(game2.scopeThroughBoard(4,"forward","A2",1),["MoveKO",""])
        self.assertEqual(game2.scopeThroughBoard(3,"forward","B1",2),['MoveOK', 'B4'])
        self.assertEqual(game2.scopeThroughBoard(3, "forward", "A2", 1), ['MoveReplace', 'C1'])
        self.assertEqual(game2.scopeThroughBoard(2, "forward", "C7", 2), ['MoveOK', 'B5'])
        self.assertEqual(game2.scopeThroughBoard(2, "forward", "C7", 1), ['MoveOK', 'A5'])
        self.assertEqual(game2.scopeThroughBoard(2,"backward", "B6",2),['MoveOK','C8'])

        # self.assertEqual(game2.scopeThroughBoard(4, "forward", "A5", 1), ['MoveOK', 'A5'])





if __name__ == '__main__':
    unittest.main()
