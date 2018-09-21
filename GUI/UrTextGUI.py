from Engine.UrEngine import *

def changePlayer(currentPlayer):
    if(currentPlayer == 1):
        newplayer = 2
    else:
        newplayer = 1
    return newplayer

def parseAction(actionInput):

    parsedAction = str.split(actionInput," ")

    if(parsedAction[0] == "AddPawn"):
        return ["AddPawn",""]
    elif(parsedAction[0] == "Move"):
        return ["Move",parsedAction[1]]
    else:
        return ["KO",""]



# create the main game
game = UrEngine()
dice = Dice()

print("Welcome to the Royal Game of Ur")

#initializing the variable that indicates if the game is ended or not
gameIsOn = True
currentPlayer = 1


#mainloop
while(gameIsOn):

    game.printGame()
    print("Your turn player %s"% (currentPlayer))
    rollresult = dice.roll()
    print("Roll of dice: %s" % (rollresult))

    actionInput = input("Actions: - AddPawn \b -Move [board square] $> ")

    action = parseAction(actionInput)
    actionResult = ""

    actionWasComplete = False
    if(rollresult == 0):
        print("The roll result was 0, next player")
    else:
        if(action[0] == "AddPawn"):
            print(action)
            actionResult = game.playerAddPawn(currentPlayer,rollresult)
            actionWasComplete = actionResult
        elif(action[0] == "Move"):
            print(action)
            moveResult = game.movePlayerPawn(rollresult,action[1],currentPlayer)
            if(moveResult == "MoveOK"):
                actionWasComplete = True
            else:
                pass
        else:
            print("action invalid")

    print("")
    if(actionResult == ""):
        print("invalid command please retry...")

    if(actionWasComplete):
        currentPlayer = changePlayer(currentPlayer)