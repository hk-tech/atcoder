import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, S, D = LI()

for i in range(N):
    x, y = LI()
    if x < S and y > D:
        print('Yes')
        exit()

print('No')