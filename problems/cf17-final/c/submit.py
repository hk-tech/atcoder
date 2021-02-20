import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
D = LI()
D.append(0)
N += 1

ans = 0
for k in range(1, 5):
    if k == 1:
        pt = 10 ** 9
        for i, j in itertools.combinations(range(N), 2):
            pt = min(pt, min(abs(D[i] - D[j]), min(D[i], D[j]) + 24 - max(D[i], D[j])))
    
    elif k == 2:
        pt = 10 ** 9
        for i, j in itertools.combinations(range(N), 2):
            pt = min(pt, min(abs(D[i] - (24 - D[j])), min(D[i], 24-D[j]) + 24 - max(D[i], 24-D[j])))
    
    if k == 3:  
        pt = 10 ** 9
        for i, j in itertools.combinations(range(N), 2):
            pt = min(pt, min(abs((24 - D[i]) - D[j]), min(24-D[i], D[j]) + 24 - max(24-D[i], D[j])))

    if k == 4:
        pt = 10 ** 9
        for i, j in itertools.combinations(range(N), 2):
            pt = min(pt, min(abs((24-D[i]) - (24-D[j])), min(24-D[i], 24-D[j]) + 24 - max(24-D[i], 24-D[j])))

    ans = max(ans, pt)
    

print(ans)