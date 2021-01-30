import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
S = []
T = []
for _ in range(N):
    S.append(input())

M = int(input())
for _ in range(M):
    T.append(input())

CS = Counter(S)
CT = Counter(T)

print(max(list((CS - CT).values()) + [0]))



