import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
A = LI()

lis = []
for i in range(1, N+1):
    lis.append([i, A[i-1]])

X = sorted(lis, key=lambda x: x[1], reverse=True)

for x in X:
    print(x[0])



