import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, K = LI()
H = LI()

ans = 0
for h in H:
    if h >= K:
        ans += 1

print(ans)


