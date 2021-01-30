import itertools
S = input()
N = int(input())

S = sorted(S)
i = 1

for x in S:
    for y in S:
        if i == N:
            print(x+y)
        i += 1