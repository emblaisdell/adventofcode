import sys

PAPER_LIMIT = 4

fname = sys.argv[1]

lines = open(fname).read().splitlines()
rolls = [[c=="@" for c in line] for line in lines]

w = len(rolls[0])
h = len(rolls)

def rollCount():
    return sum(rolls[y][x] for x in range(w) for y in range(h))

startRollCount = rollCount()

def hasPaper(x,y):
    return x in range(w) and y in range(h) and rolls[y][x]

def accessible(x,y):
    return hasPaper(x,y) and sum(hasPaper(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2)) <= PAPER_LIMIT


oldRolls = []

while rolls != oldRolls:
    oldRolls = rolls
    rolls = [[hasPaper(x,y) and not accessible(x,y) for x in range(w)] for y in range(h)]

endRollCount = rollCount()

# print("\n".join(["".join(["@" if rolls[y][x] else "." for x in range(w)]) for y in range(h)]))

print(startRollCount - endRollCount)
