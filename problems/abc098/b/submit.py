import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
S = input()
ans = 0
for i in range(1, N-1):
    c1 = Counter(S[:i])
    c2 = Counter(S[i:])

    if len(c1) >= len(c2):
        clarge = c1
        csmall = c2
    else:
        csmall = c1
        clarge = c2

    tmp = 0
    for x in csmall:
        if x in clarge:
            tmp += 1

    ans = max(ans, tmp)

print(ans)


