import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

H, W = LI()
ans = 0
arr = [list(input()) for i in range(H)]
for i in range(H-1):
    for j in range(W-1):
        cnt = 0
        for x in (arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1]):
            if x == '#':
                cnt += 1
        if cnt in (1, 3):
            ans += 1

print(ans)

