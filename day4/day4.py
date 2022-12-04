elfPairLocation = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day4/input.txt'
elfPairs = list(filter(None, open(elfPairLocation, 'r').read().split('\n')))

taskContains = 0
taskOverlaps = 0

def getListRange(startValue, endValue):
    if (startValue == endValue):
        return [startValue]
    else:
        return list(range(startValue, endValue+1))

for elves in elfPairs:
   group1, group2 = elves.split(',')
   start1, end1 = [eval(position) for position in  group1.split('-')]
   start2, end2 = [eval(position) for position in  group2.split('-')]
   if (start2 >= start1) and (end1 >= end2) or (start1 >= start2) and (end2 >= end1):
        taskContains += 1
   if (set(getListRange(start1, end1)).intersection(getListRange(start2, end2))):
        taskOverlaps += 1

# Day 4
print(taskContains) 

# Part 2
print(taskOverlaps)