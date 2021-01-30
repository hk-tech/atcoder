N, X = (int(i) for i in input().split())

alc = 0
for i in range(N):
    v, p = (int(i) for i in input().split())
    alc += v * p
    if alc > X * 100:
        print(i+1)
        exit()

print('-1')