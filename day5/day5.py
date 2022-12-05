from collections import defaultdict
import copy
shippingManifestLocation = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day5/input.txt'
shippingManifest = open(shippingManifestLocation, 'r').readlines()

def getCrateSortingInfo(crateList):
    global totalRows
    totalRows = 0
    global crateRowNumbers 
    crateRowNumbers = []
    rowSize = 1

    for i in range(0, len(crateList)):
        rowSize += 1
        if crateList[i] != " ":
            totalRows += 1
            crateRowNumbers.append(int(crateList[i]))
    return rowSize / totalRows;

crates = []
instructions = []

reachedInstructions = False
for line in shippingManifest:
    if line.strip():
        line = line.replace("\n", "")
        if reachedInstructions:
            instructions.append(line)
        else: 
            crates.append(line)
    else:
        reachedInstructions = True

crateRowSize = getCrateSortingInfo(crates[len(crates) - 1])
crateDictionary = defaultdict(list)
crateDictionary.update((number, []) for number in crateRowNumbers)
crates = crates[:-1]

def sortCratesIntoDictonary(crateRow):
    for i in range(0, len(crateRow)):
        if crateRow[i].isalpha():
            dictonaryPosition = (i / crateRowSize).__floor__() + 1
            crateDictionary[dictonaryPosition].append(crateRow[i])

for crateRow in crates:
    sortCratesIntoDictonary(crateRow)

crate9001Dictionary = copy.deepcopy(crateDictionary)

def sortByCraneType(newCrane, list1, list2):
    if (newCrane):
        return list1 + list2
    else:
        return list(reversed(list1)) + list2

def crateSortingCrane(craneMove, dictionary, newCrane=False):
    amount, startPosition, endPosition = [int(move) for move in craneMove.split() if move.isdigit()]
    moveItems = sortByCraneType(newCrane, dictionary[startPosition][:amount], dictionary[endPosition])
    dictionary.update({endPosition: moveItems})
    del dictionary[startPosition][:amount]

for craneMove in instructions:
    crateSortingCrane(craneMove, crateDictionary)
    crateSortingCrane(craneMove, crate9001Dictionary, True)

def generateCraneCode(dictonary):
    craneCode = []
    for i in crateRowNumbers:
        craneCode.append(dictonary[i][0])  
    return "".join(craneCode)

# Day 5
print(generateCraneCode(crateDictionary))

# Part 2
print(generateCraneCode(crate9001Dictionary))
