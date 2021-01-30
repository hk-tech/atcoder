import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, M = LI()

AB = [[int(i) for i in input().split()] for i in range(M)]

K = int(input())
CD = [[int(i) for i in input().split()] for i in range(K)]

ans = 0
for mask in range(2 ** K):
    lis = []
    for i in range(K):  # このループが一番のポイント
        lis.append(CD[(mask >> i) & 1])

    for a, b in AB:
        if a in lis and b in lis:
            ans += 1

print(ans)


