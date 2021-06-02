import random

playerWins = 0
computerWins = 0
ties = 0
userChoice = ""


def playerChoice():

    cont = False
    count = 0
    while cont == False:
        global userChoice
        userChoice = input(
            "Pick your move! Rock, Paper, Scissors? Or \"Quit\" to quit.")

        if userChoice[0] == "r" or userChoice[0] == "R":
            userChoice = 1
            cont = True
            count = count + 1
        elif userChoice[0] == "p" or userChoice[0] == "P":
            userChoice = 2
            cont = True
            count = count + 1
        elif userChoice[0] == "s" or userChoice[0] == "S":
            userChoice = 3
            cont = True
            count = count + 1
        elif userChoice == "Quit":
            # userChoice = "Quit"
            cont = True
        else:
            cont = False
            print("Invalid input... try again")
    # print(userChoice)
    return userChoice


def computerChoice():
    computerChoice = random.randint(1, 3)
    return computerChoice


def results(userChoice, computerChoice):

    if (userChoice == 1):
        print("You picked Rock.")
    elif (userChoice == 2):
        print("You picked Paper.")
    elif (userChoice == 3):
        print("You picked Scissors.")

    if (computerChoice == 1):
        print("Computer picked Rock.")
    elif (computerChoice == 2):
        print("Computer picked Paper.")
    elif (computerChoice == 3):
        print("Computer picked Scissors.")

    if userChoice == computerChoice:
        print("It's a tie!\n")
        global ties
        ties += 1
    elif (userChoice == 1 and computerChoice == 3) or (userChoice == 2 and computerChoice == 1) or (userChoice == 3 and computerChoice == 2):
        print("Player wins!\n")
        global playerWins
        playerWins += 1
    else:
        print("Computer wins!\n")
        global computerWins
        computerWins += 1

    print("Player wins: " + str(playerWins) +
          " -- Computer wins: " + str(computerWins) + " -- Ties: " + str(ties))


def playRound():
    global userChoice
    count = 0

    while (userChoice != "Quit"):
        print("Round " + str(count))
        # print(userChoice)
        userChoice = playerChoice()
        # print(userChoice)

        if (userChoice != "Quit"):
            pcChoice = computerChoice()
            results(userChoice, pcChoice)
            count += 1


def playGame():
    playRound()


playGame()
