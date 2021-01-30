N, M = (int(i) for i in input().split())
lis = [-1] * N

for i in range(M):
    s, c = (int(i) for i in input().split())

    if lis[s-1] < 0:
        lis[s-1] = c
    else:
        if lis[s-1] != c:
            print(-1)
            exit()

    if s == 1 and c == 0 and N > 1:
        print(-1)
        exit()

for i in range(N):
    if lis[i] < 0:
        if i == 0:
            if N == 1:
                lis[i] = '0'
            else:
                lis[i] = '1'
        else:
            lis[i] = '0'
    else:
        lis[i] = str(lis[i])

print(''.join(lis))

