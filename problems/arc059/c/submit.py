import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
import numpy as np
N = int(input())
A = LI()

m = np.mean(A)
f = math.floor(m)
c = math.ceil(m)

fans, cans = (0, 0)
for i in range(N):
    fans += (A[i] - f) ** 2
    cans += (A[i] - c) ** 2

print(min(fans, cans))
    


