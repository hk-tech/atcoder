import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
A = LI()

cum = [A[0]]

if N == 2:
    print(abs(A[0] - A[1]))
    exit()

for i in range(1, N):
    cum.append(cum[i-1] + A[i])

ans = 10 ** 9
for i in range(N-2):
    ans = min(ans, abs(cum[i] - (cum[N-1]-cum[i])))

print(ans)

