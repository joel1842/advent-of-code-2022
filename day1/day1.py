elfSnacks = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day1/input.txt'
allTheElves = open(elfSnacks, 'r').read().split('\n\n'); 
hungriestElfList = []
for elf in allTheElves: hungriestElfList.append(sum([int (elf) for elf in elf.split("\n") if elf]))
# Part One
print(max(hungriestElfList))
# Part Two
print(sum(sorted(hungriestElfList, reverse=True)[:3]))

