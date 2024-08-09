import random

gameOptions = ["Rock", "Paper", "Scissors"]

possibleOutcomes = {
    "0:0":"Draw",
    "0:1":"Player",
    "0:2":"Computer",
    "1:0":"Computer",
    "1:1":"Draw",
    "1:2":"Player",
    "2:0":"Player",
    "2:1":"Computer",
    "2:2":"Draw"
}

playerWins = 0
computerWins = 0
gameDraws = 0

while(True):

    gameCounterText = "******\nComputer: {}, Draws: {}, Player: {}\n*******"
    print(gameCounterText.format(computerWins, gameDraws, playerWins))

    userInput = int(input('Rock[0], Paper[1], Scissors[2]: '))

    if userInput not in range(0,3):
        print('Entry out of range (0,3)... Try again!')
        continue

    userOption = gameOptions[userInput]
    randomOption = random.randint(0,2)

    gameKey = f"{randomOption}:{userInput}"
    gameResult = possibleOutcomes[gameKey]

    if(gameResult == 'Draw'):
        gameDraws += 1
        output = "===\nComputer: {} | Player: {} \nResult: Draw!!!\n==="
        print(output.format(gameOptions[randomOption], gameOptions[userInput]))
        continue;

    if(gameResult == 'Computer'):
        computerWins += 1
        output = "===\nComputer: {} | Player: {} \nResult: Computer Wins!!!\n==="
        print(output.format(gameOptions[randomOption], gameOptions[userInput]))
        continue;

    if(gameResult == 'Player'):
        playerWins += 1
        output = "===\nComputer: {} | Player: {} \nResult: Player Wins!!!\n==="
        print(output.format(gameOptions[randomOption], gameOptions[userInput]))
        continue;
