import string
rucksackLocation = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day3/input.txt'
openRucksacks = open(rucksackLocation, 'r').read()
rucksacks = list(filter(None, openRucksacks.split('\n')))

alphabet = list(string.ascii_letters)
rucksackDictionary = dict(zip(alphabet, list(range(1, len(alphabet) + 1))))

overlappingRucksackItems = []
for items in rucksacks:
    firstCompartment, secondCompartment = items[:len(items)//2], items[len(items)//2:]
    overlappingItem = rucksackDictionary[''.join(set(firstCompartment).intersection(secondCompartment))]
    overlappingRucksackItems.append(overlappingItem)
    
# Day 1 
print(sum(overlappingRucksackItems))

elfGroups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
elfBadges = []
for rucksacks in elfGroups:
    elfBadge = rucksackDictionary[''.join(set.intersection(*map(set, rucksacks)))]
    elfBadges.append(elfBadge)
    
# Part 2
print(sum(elfBadges))
