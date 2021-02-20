import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N, K = LI()
S = list(str(N))

def f(S):
    return int(''.join(sorted(S, reverse=True))) - int(''.join(sorted(S)))

ans = f(S)
if K == 0:
    print(N)
    exit()
if K == 1:
    print(ans)
    exit()
for i in range(K-1):
    tmp = list(str(ans))
    ans = f(tmp)

print(ans)



