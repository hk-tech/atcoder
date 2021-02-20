import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

S = int(input())
mod = 10 ** 9 + 7

lis = [-1] * 2001
def solve(N):
    if lis[N] >= 0:
        return lis[N] 

    if N <= 2:
        ret = -1
    elif N <= 5:
        ret = 0
    else:
        ret = 0
        for x in range(3, 1998):
            if N - x >= 1:
                ret += solve(N-x)

    lis[N] = (ret+1) % mod
    #print(N, ret+1)
    return (ret+1) % mod

print(solve(S))
        