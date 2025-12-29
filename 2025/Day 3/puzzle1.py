import sys

fname = sys.argv[1]

# Returns the first index of the max value
def argmax(l):
    print(f"argmax {l}")
    return l.index(max(l))


def total_joltage(bank, n):
    if n == 0:
        return 0
    i = argmax(bank[:len(bank)-(n-1)])
    return 10**(n-1)*int(bank[i]) + total_joltage(bank[i+1:], n-1)


def main():
    lines = open(fname).read().splitlines()
    print(sum(total_joltage(list(line), 12) for line in lines))


main()
