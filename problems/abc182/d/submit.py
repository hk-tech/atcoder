N = int(input())
A = list(map(int, input().split()))

S = [0]
cumA = [0]
cnt = A[0]
ans = max(0, A[0])
for i in range(N):
    cumA.append(cumA[i] + A[i])
    S.append(S[i] + cumA[i+1])
    cnt = max(cnt, cumA[i])
    ans = max(ans, S[i] + cnt)  
ans = max(ans, S[-1])
print(ans)