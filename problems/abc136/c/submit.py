import sys, math, itertools
import numpy as np
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
H = LI()

m = 0
for i in range(N):
    if H[i] < m - 1:
        print('No')
        exit()

    m = max(m, H[i])

print('Yes')