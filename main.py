print("Lets play Tic Tac Toe!")

game_active = True
current_player = "X"

gamefield = [" ",
            "1","2","3",
            "4","5","6",
            "7","8","9"]

def printField():
    print (gamefield[1] + "|" + gamefield[2] + "|" + gamefield[3])
    print (gamefield[4] + "|" + gamefield[5] + "|" + gamefield[6])
    print (gamefield[7] + "|" + gamefield[8] + "|" + gamefield[9])

def playerInput():
    global game_active
    while True:
        move = input("Please select your field:")

        if move == "q":
            game_active = False
            return
        try:
            move = int(move)
        except ValueError:
            print("Please select a number between 1 and 9")
        else:
            if move >= 1 and move <= 9:
                if(gamefield[move] == "X" or gamefield[move] == "O"):
                    print("This field is already taken! Please select another one!")
                else:
                    return move
            else:
                print("Please select a number between 1 and 9")

def changePlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def checkWin():
    if gamefield[1] == gamefield[2] == gamefield[3]:
        return gamefield[1]
    if gamefield[4] == gamefield[5] == gamefield[6]:
        return gamefield[4]
    if gamefield[7] == gamefield[8] == gamefield[9]:
        return gamefield[7]
    # Kontrolle auf Spalten
    if gamefield[1] == gamefield[4] == gamefield[7]:
        return gamefield[1]
    if gamefield[2] == gamefield[5] == gamefield[8]:
        return gamefield[2]
    if gamefield[3] == gamefield[6] == gamefield[9]:
        return gamefield[3]
    # Kontrolle auf Diagonalen
    if gamefield[1] == gamefield[5] == gamefield[9]:
        return gamefield[5]
    if gamefield[7] == gamefield[5] == gamefield[3]:
        return gamefield[5]

def checkTie():
    if (gamefield[1] == 'X' or gamefield[1] == 'O') \
      and (gamefield[2] == 'X' or gamefield[2] == 'O') \
      and (gamefield[3] == 'X' or gamefield[3] == 'O') \
      and (gamefield[4] == 'X' or gamefield[4] == 'O') \
      and (gamefield[5] == 'X' or gamefield[5] == 'O') \
      and (gamefield[6] == 'X' or gamefield[6] == 'O') \
      and (gamefield[7] == 'X' or gamefield[7] == 'O') \
      and (gamefield[8] == 'X' or gamefield[8] == 'O') \
      and (gamefield[9] == 'X' or gamefield[9] == 'O'):
        return ('tie')

printField()

while game_active:
    print()
    print("Its Player " + current_player + "'s turn")
    move = playerInput()
    if move:
        gamefield[move] = current_player
        printField()
        win = checkWin()

        if win:
            print("Player " + current_player + " won the game")
            game_active = False
            break
        tie = checkTie()

        if tie:
            print("No one won! Its a tie!")
            game_active = False
            
        changePlayer()

input()