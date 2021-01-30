import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())

XY = [[int(i) for i in input().split()] for i in range(N)]

ans = 0
for i, j in itertools.combinations(range(N), 2):
    ans = max(ans, math.sqrt(pow(XY[i][0]-XY[j][0], 2) + pow(XY[i][1]-XY[j][1], 2)))

print(ans)



