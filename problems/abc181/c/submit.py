N = int(input())
XY = [[int(i) for i in input().split()] for i in range(N)]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            xk, yk = XY[k]

            if yj - yi != 0 and yk - yi != 0:
                if (xj - xi)/(yj - yi) == (xk - xi)/(yk - yi) or (xi == xj and xj == xk):
                    print('Yes')
                    exit()
            else:
                if yi == yj and yj == yk:
                    print('Yes')
                    exit()

print('No')