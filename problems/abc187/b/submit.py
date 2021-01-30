N = int(input())
XY = [[int(i) for i in input().split()] for i in range(N)]

import itertools
ans = 0
for (x1, y1), (x2, y2) in itertools.combinations(XY, 2):
    k = (y2 - y1) / (x2- x1)

    if k >= -1 and k <= 1:
        ans += 1

print(ans)
