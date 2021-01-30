import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
N, M = (int(i) for i in input().split())

v = [[] for i in range(N)] [[1, 2, 3], [2, 4], ]
for i in range(M):
    a, b = LI()
    a -= 1
    b -= 1
    if b not in v[a]:
        v[a].append(b)
        v[b].append(a)

for i in range(N):
    s = []
    for x in v[i]:
        for y in v[x]:
            if y not in v[i]+[i]:
                s.append(y)
    print(len(set(s)))






