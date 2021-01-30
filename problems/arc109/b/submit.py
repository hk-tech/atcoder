N = int(input())

l = 1
r = 10 ** 18 + 1

while abs(l-r) > 1:
    mid = (l + r) // 2
    if (mid + 1) * mid // 2 <= N + 1:
        l = mid
    else:
        r = mid

print(N - l + 1)