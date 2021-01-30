X, Y = (int(i) for i in input().split())

if X % Y == 0:
    print('-1')
else:
    for i in range(1, 10 ** 18):
        if (i * X) % Y != 0:
            print(i * X)
            exit()