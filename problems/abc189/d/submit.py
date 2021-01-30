N = int(input())
dp = [0] * (N+1)
dp[0] = 1
for i in range(N):
    s = input()
    if s == 'OR':
        dp[i+1] = 2 ** (i+1) + dp[i]
    else:
        dp[i+1] = dp[i]

print(dp[N])