N = int(input())

lis = []
sumA = 0
for i in range(N):
    a, b = map(int, input().split())
    c = 2 * a + b
    lis.append((a, b, c))
    sumA += a

lis = sorted(lis, key=lambda x: x[2])[::-1]

ans = 0
for a, b, c in lis:
    sumA -= c 
    ans += 1
    if sumA < 0:
        print(ans)
        exit()

print(1)