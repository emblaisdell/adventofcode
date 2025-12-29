import sys

PAPER_LIMIT = 4

fname = sys.argv[1]

LINES = open(fname).read().splitlines()

w = len(LINES[0])
h = len(LINES)

def hasPaper(x,y):
    return x in range(w) and y in range(h) and LINES[y][x] == "@"

def accessible(x,y):
    return hasPaper(x,y) and sum(hasPaper(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2)) <= PAPER_LIMIT


# print("\n".join(["".join([("x" if accessible(x,y) else "@") if hasPaper(x,y) else "." for x in range(w)]) for y in range(h)]))

print(sum(accessible(x,y) for x in range(w) for y in range(h)))
