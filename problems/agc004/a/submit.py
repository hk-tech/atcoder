import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

X = LI()
X.sort()
A, B, C = X

if C % 2 == 0:
    print(0)
else:
    print(A * B)



