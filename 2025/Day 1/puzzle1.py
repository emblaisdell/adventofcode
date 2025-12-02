import sys

fname = sys.argv[1]

MODULUS = 100

pointer = 50
accumulator = 0

for line in open(fname).read().splitlines():
    rest = line[1:]
    match line[0]:
        case "L":
            pointer -= int(rest)
        case "R":
            pointer += int(rest)
        case _:
            raise Exception(f"Invalid initial value {line[0]}")
    pointer %= MODULUS
    if pointer == 0:
        accumulator += 1

print(f"Accumulator = {accumulator}")