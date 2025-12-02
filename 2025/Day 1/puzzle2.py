import sys

fname = sys.argv[1]

MODULUS = 100

pointer = 50
accumulator = 0

def move(dir):
    global pointer, accumulator
    pointer += dir
    pointer %= MODULUS
    if pointer == 0:
        accumulator += 1

for line in open(fname).read().splitlines():
    # print(f"{pointer}, {accumulator}")
    wasZero = pointer == 0
    rest = line[1:]
    match line[0]:
        case "L":
            for _ in range(int(rest)):
                move(-1)
        case "R":
            for _ in range(int(rest)):
                move(1)
        case _:
            raise Exception(f"Invalid initial value {line[0]}")

print(f"Accumulator = {accumulator}")
