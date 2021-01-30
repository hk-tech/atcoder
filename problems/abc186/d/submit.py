N = int(input())
A = list(map(int, input().split()))
A.sort()

cumA = [0]

for i in range(0, N):
    cumA.append(cumA[i] + A[i])

ans = 0
for i in range(0, N):
    ans += A[i] * i - cumA[i]

print(ans)