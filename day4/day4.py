elfPairLocation = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day4/input.txt'
elfPairs = list(filter(None, open(elfPairLocation, 'r').read().split('\n')))

taskContains = 0
for elves in elfPairs:
   group1, group2 = elves.split(',')
   start1, end1 = [eval(position) for position in  group1.split('-')]
   start2, end2 = [eval(position) for position in  group2.split('-')]
   if (start2 >= start1) and (end1 >= end2) or (start1 >= start2) and (end2 >= end1):
        taskContains += 1

# Day 4
print(taskContains) 