from collections import deque, defaultdict, Counter

N = int(input())
S = []
for _ in range(N):
    S.append(input())

c = Counter(S)

lis = []
m = max(c.values())
for x in c:
    if c[x] == m:
        lis.append(x)

lis.sort()

for x in lis:
    print(x)