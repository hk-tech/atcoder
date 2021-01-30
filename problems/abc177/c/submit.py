N = int(input())
mod = 10 ** 9 + 7
A = list(map(int, input().split()))

cum = [A[0]]

for i in range(1, N):
    cum.append(cum[i-1] + A[i])

ans = 0
for i in range(N):
    ans += A[i] * (cum[N-1] - cum[i])

print(ans%mod)