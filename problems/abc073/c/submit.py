import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

c = Counter(A)

ans = 0
for k in c.keys():
    if c[k] % 2 == 1:
        ans += 1

print(ans)


