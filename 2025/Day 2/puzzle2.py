import sys
import math

fname = sys.argv[1]

accumulator = 0

def repeatsNTimes(s, n):
    l = len(s)
    if l%n != 0:
        return False
    m = l // n
    for i in range(m, l, m):
        if s[i:i+m] != s[:m]:
            return False
    return True

def repeats(s):
    return any((repeatsNTimes(s,n) for n in range(2,len(s) + 1)))

def invalid(n):
    return repeats(str(n))


rangesStr = open(fname).read()

for rng in rangesStr.split(","):
    [start,end] = rng.split("-")
    for n in range(int(start),int(end)+1):
        if invalid(n):
            accumulator += n

print(accumulator)
