communicationSignal = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day6/input.txt'
communicationReciever = open(communicationSignal, 'r').read()
startOfPacket = None
for char in range(0, len(communicationReciever)):
    if startOfPacket == None and len(set(communicationReciever[char-4:char])) == 4: startOfPacket = char

# Day 6            
print(startOfPacket)

