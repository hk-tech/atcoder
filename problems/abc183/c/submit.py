N, K = (int(i) for i in input().split())
T = [[int(i) for i in input().split()] for i in range(N)]

import itertools

ans = 0
for lis in itertools.permutations(range(1, N)):
    i = 0
    total = 0
    for x in lis:
        total += T[i][x]
        i = x

    total += T[x][0]
    if total == K:
        ans += 1

print(ans)
    
