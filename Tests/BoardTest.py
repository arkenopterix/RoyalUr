from Objects.Board import *
import unittest


class TestBoardMethods(unittest.TestCase):

    def testBoard_checkIsValidPosition(self):
        board= Board()
        self.assertFalse(board.checkIsValidPosition("D34"))
        self.assertTrue(board.checkIsValidPosition("C8"))


    def testBoard_placePawn(self):
        board1 = Board()

        self.assertEqual(board1.placePawn(1, "A11"), "invalid position")

        self.assertEqual(board1.placePawn(2,"B2"),"MoveOK")
        self.assertEqual(board1.placePawn(1, "A1"),"MoveOK")

        self.assertEqual(board1.boardDic["B2"][0],2)
        self.assertEqual(board1.boardDic["A1"][0],1)

        self.assertEqual(board1.placePawn(2,"B2"),"MoveKO")


    def testBoard_removePawn(self):
        board2 = Board()
        board2.placePawn(2, "B2")
        self.assertEqual(board2.placePawn(1, "A11"), "invalid position")
        self.assertEqual(board2.removePawn("B2"), "OK")
        self.assertEqual(board2.boardDic["B2"][0], 0)


    def testBoard_getSquareState(self):
        board3 = Board()
        board3.placePawn(2, "B2")
        self.assertEqual(board3.getSquareState("B2"), 2)

    def testBoard_getNextSquare(self):
        board4 = Board()
        self.assertEqual(board4.getNextSquare(3, "A4"), "invalid player number")
        self.assertEqual(board4.getNextSquare(1, "A43"), "invalid position")
        self.assertEqual(board4.getNextSquare(1,"A4"), "C1")
        self.assertEqual(board4.getNextSquare(1, "C8"), "A5")
        self.assertEqual(board4.getNextSquare(2, "C8"), "B5")

    def testBoard_getPreviousSquare(self):
        board5= Board()
        self.assertEqual(board5.getPreviousSquare(1,"A5"),"C8")
        self.assertEqual(board5.getPreviousSquare(1, "B5"), "C8")

    def testBoard_getIsSpecialSquare(self):
        board6= Board()
        self.assertEqual(board6.isSpecialSquare("C4"),True)
        self.assertEqual(board6.isSpecialSquare("C8"),False)

if __name__ == '__main__':
        unittest.main()