
N, K = (int(i) for i in input().split())
ans = 0

def calc(n):
    return min(n-1, 2 * N + 1 - n)

for x in range(2, 2 * N + 1):
    y = x - K

    if y >= 2 and y <= 2 * N:
        ans += calc(x) * calc(y)

print(ans)
