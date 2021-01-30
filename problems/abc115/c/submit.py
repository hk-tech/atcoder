N, K = (int(i) for i in input().split())
H = []
for i in range(N):
    H.append(int(input()))

H.sort(reverse=True)

ans = 100000000000
for i in range(N-K+1):
    ans = min(ans, H[i]-H[i+K-1])

print(ans)