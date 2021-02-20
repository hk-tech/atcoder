import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, X = LI()
A = LI()

AA = [i for i in A if i != X]

print(*AA)



