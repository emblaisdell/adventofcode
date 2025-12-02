import sys

fname = sys.argv[1]

accumulator = 0

def invalid(n):
    s = str(n)
    l = len(s)
    if l%2 != 0:
        return False
    return s[:l//2] == s[l//2:]

for rng in open(fname).read().split(","):
    [start,end] = rng.split("-")
    for n in range(int(start),int(end)+1):
        if invalid(n):
            accumulator += n

print(accumulator)