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
        
    match realmove:
        case "A": 
            if (cheatmove == "Y"): roundScore.append(6)
        case "B": 
            if (cheatmove == "Z"): roundScore.append(6)
        case "C": 
            if (cheatmove == "X"): roundScore.append(6)

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

def newScore(mymove, increment):
    score = gameScoreDictionary[mymove] + increment
    if (score < 1):
        score = 3
    if (score > 3):
        score = 1
    match mymove:
        case "X": 
            return 0 + score
        case "Y": 
            return 3 + score
        case "Z": 
            return 6 + score

def newElfReferee(elfmove, mymove):
    match elfmove:
        case "A": 
            return newScore(mymove, -1);
        case "B": 
            return newScore(mymove, 0);
        case "C": 
            return newScore(mymove, 1);

for move in cheatBook: 
    if len(move) > 0:
        moveList = move.split()
        newStrategyScore.append(newElfReferee(moveList[0], moveList[1]))

print(sum(newStrategyScore))
