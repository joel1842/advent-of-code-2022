communicationSignal = '/Users/joellake/Documents/GitHub/advent-of-code-2022/day6/input.txt'
communicationReciever = open(communicationSignal, 'r').read()
startOfPacket = None
startOfMessage = None
for char in range(0, len(communicationReciever)):
    if startOfPacket == None and len(set(communicationReciever[char-4:char])) == 4: startOfPacket = char
    if startOfMessage == None and len(set(communicationReciever[char-14:char])) == 14: startOfMessage = char

# Day 6            
print(startOfPacket)

# Part 2
print(startOfMessage)
