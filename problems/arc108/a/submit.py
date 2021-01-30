S, P = (int(i) for i in input().split())

for m in range(1, 10 ** 6 + 1):
    if (S-m) * m == P:
        print('Yes')
        exit()

print('No')