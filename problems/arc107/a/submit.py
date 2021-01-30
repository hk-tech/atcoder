A, B, C = (int(i) for i in input().split())

X = (1 + C) * C // 2
Y = (X + X * B) * B // 2
ans = (Y + Y * A) * A // 2
mod = 998244353
print(ans%mod)