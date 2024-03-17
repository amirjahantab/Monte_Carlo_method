import random
import sys

n = int(sys.argv[1])
trials = int(sys.argv[2])

s = []
for i in range(trials):
    count = 0
    collected_count = 0
    is_collected = [False] * n

    while True:
        if collected_count == n:
            s += [count]
            break

        count += 1
        value = random.randrange(0, n)

        if not is_collected[value]:
            collected_count += 1
            is_collected[value] = True

print(sum(s) // len(s))
