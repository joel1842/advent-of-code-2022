strategyGuide = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day2/input.txt'
cheatBook = open(strategyGuide, 'r').read().split('\n')
gameScoreDictionary = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def elfReferee(realmove, cheatmove):
    roundScore = [gameScoreDictionary[cheatmove]]
    if (gameScoreDictionary[realmove] == gameScoreDictionary[cheatmove]):
        roundScore.append(3)

    def win():
        roundScore.append(6)

    match realmove:
        case "A": 
            if (cheatmove == "Y"): win()
        case "B": 
            if (cheatmove == "Z"): win()
        case "C": 
            if (cheatmove == "X"): win()
    print(realmove, cheatmove, sum(roundScore))
    return sum(roundScore);

allTheMoves = []
for move in cheatBook: 
    if len(move) > 0:
        moveList = move.split()
        allTheMoves.append(elfReferee(moveList[0], moveList[1]))

# Day 1
print(sum(allTheMoves))

# Part 2
newStrategyScore = []

def decideOutcome(mymove):
    match mymove:
        case "X": 
            return 0
        case "Y": 
            return 3
        case "Z": 
            return 6

def newElfReferee(elfmove, mymove):
    roundScore = []
    match elfmove:
        case "A": 
            if (mymove == "X"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["Z"])
            if (mymove == "Y"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["X"])
            if (mymove == "Z"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["Y"])
        case "B": 
            if (mymove == "X"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["X"])
            if (mymove == "Y"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["Y"])
            if (mymove == "Z"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["Z"])
        case "C": 
            if (mymove == "X"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["Y"])
            if (mymove == "Y"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["Z"])
            if (mymove == "Z"): roundScore.append(decideOutcome(mymove) + gameScoreDictionary["X"])

    print(elfmove, mymove, sum(roundScore))
    return sum(roundScore);

for move in cheatBook: 
    if len(move) > 0:
        moveList = move.split()
        newStrategyScore.append(newElfReferee(moveList[0], moveList[1]))

print(sum(newStrategyScore))
