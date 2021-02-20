import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, M, T = LI()

bat = N
for i in range(M):
    A, B = LI()
    bat = min(N-A+(B-A)*2, N)
    print(bat)

bat -= T - B    

if bat <= 0:
    print('No')
else:
    print('Yes')
