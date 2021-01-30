N, M = (int(i) for i in input().split())
B = [[int(i) for i in input().strip()] for i in range(N)]
ans = [[0 for j in range(M)] for i in range(N)]

for i in range(1, N-1):
    for j in range(1, M-1):
        ans[i][j] = B[i-1][j]
        B[i-1][j] -= ans[i][j]
        B[i][j-1] -= ans[i][j]
        B[i][j+1] -= ans[i][j]
        B[i+1][j] -= ans[i][j]

for i in range(N):
    print(''.join([str(x) for x in ans[i]]))

