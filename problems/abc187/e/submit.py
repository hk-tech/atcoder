import sys
from collections import deque
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
v = [[] for i in range(N)]
edges = []
for i in range(N-1):
    a, b = LI()
    a -= 1
    b -= 1
    edges.append((a, b))
    v[a].append(b)
    v[b].append(a)

depth = [-1] * N
depth[0] = 0
q = [0]

while q:
    at = q.pop()
    for i in v[at]:
        if depth[i] == -1:
            depth[i] = depth[at] + 1 
            q.append(i)

ans = [0] * N
Q = int(input())
for i in range(Q):
    t, e, x = LI()
    a, b = edges[e-1]
    if depth[a] > depth[b]:
        a, b = b, a
        if t == 1:
            t = 2
        else:
            t = 1

    if t == 1:
        ans[0] += x
        ans[b] -= x
    else:
        ans[b] += x

q = [0]
while q:
    at = q.pop()
    for i in v[at]:
        if depth[at] < depth[i]:
            ans[i] += ans[at]
            q.append(i)


for x in ans:
    print(x)
    
