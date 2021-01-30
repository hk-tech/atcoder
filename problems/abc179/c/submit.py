N = int(input())

lis = [0] * N
ans = 0

for i in range(1, N + 1):
    for j in range(1, N//i+1):
        if i * j <= N - 1:
            lis[i*j] += 1

print(sum(lis))
