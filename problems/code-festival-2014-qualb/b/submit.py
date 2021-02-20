import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, K = LI()

walk = 0
for i in range(N):
    walk += int(input())

    if walk >= K:
        print(i+1)
        exit()


