import sys, math, itertools
from collections import deque, defaultdict, Counter
from decimal import *
sys.setrecursionlimit(10**9)
def LI(): return [Decimal(x) for x in sys.stdin.readline().split()]

X, Y, R = LI()

ans = 0
for i in range(math.ceil(X-R), math.floor(X+R)+1):
    p = (R ** 2 - (i-X) ** 2).sqrt()
    h = math.floor(Y + p)
    l = math.ceil(Y - p)
    ans += int(h - l + 1)

print(ans)




