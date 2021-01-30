N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = A[0]
cnt = [-2] * N
num = 0
i = 1
while num < N-2: 
    ans += A[i]
    cnt[i] += 1
    
    if cnt[i] == 0:
        i += 1
    num += 1

print(ans)