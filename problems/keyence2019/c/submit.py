import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
A = LI()
B = LI()

sumA = sum(A)
sumB = sum(B)

if sumA < sumB:
    print('-1')
else:
    D = []
    minus = 0
    ans = 0
    for i in range(N):
        d = A[i] - B[i]
        if d >= 0:
            D.append(d)
        else:
            minus += d
            ans += 1

    D.sort(reverse=True)

    d = deque(D)
    while minus < 0:
        x = d.popleft()
        minus += x
        ans += 1

    print(ans)


