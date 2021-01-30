import sys
N, C = (int(i) for i in input().split())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

e = []
for i in range(N):
    a, b, c = LI()
    e.append((a, c))
    e.append((b+1, -c))

e.sort()

ans, total, prev = 0, 0, 0
for day, diff in e:
    ans += (day - prev) * min(total, C)
    prev = day
    total += diff

print(ans)


