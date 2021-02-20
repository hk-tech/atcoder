import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

S = input()
N = len(S)

for i in range(N):
    s = S[i]
    if i % 2 == 0:
        if s.lower() == s:
            continue
        else:
            print('No')
            exit()
    else:
        if s.lower() != s:
            continue
        else:
            print('No')
            exit()

print('Yes')



