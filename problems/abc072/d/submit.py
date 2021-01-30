from collections import deque
N = int(input())
P = list(map(int, input().split()))
#P = [2, 4, 3, 5, 8, 6, 1, 7, 9, 11, 11, 10]

i = 1
lis = []
for p in P:
    if p == i:
        lis.append(1)
    else:
        lis.append(0)
    i += 1
total = sum(lis)

d = deque(lis)
ans = 0
while d:
    x = d.pop()
    if x == 1:
        if d:
            nxt = d.pop()
            if nxt == 1:
                ans += 1
                total -= 2
            else:
                ans += 1
                total -= 1
print(ans + total)