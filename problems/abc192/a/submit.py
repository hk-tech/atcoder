import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

X = int(input())

if X % 100 == 0:
    print(100)
else:
    print((X - X%100)+100-X)





