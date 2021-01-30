N = int(input())
mod=1000000007

ans = 10 ** N - (9 ** N * 2 - 8 ** N)
print(ans%mod)