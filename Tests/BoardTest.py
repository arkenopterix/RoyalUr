from Objects.Board import *

board = Board()
print("___________________Print test______________________")
board.show()
print("___________________Placement test______________________")
print(board.placePawn(2,"B2"))
print(board.placePawn(1,"A1"))

board.show()

print("___________________replacement test______________________")

print(board.placePawn(2,"C2"))
board.show()
print(board.placePawn(1,"C2"))
board.show()