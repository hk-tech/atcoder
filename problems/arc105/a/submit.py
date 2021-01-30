import itertools
A, B, C, D = (int(i) for i in input().split())
lis = [A, B, C, D]
N = 4
org_total = sum(lis)

for mask in range(2 ** N):
    total = 0
    for i in range(N):
        if ((mask >> i) & 1): 
            total += lis[i]

    if total == org_total - total:
        print('Yes')
        exit()

print('No')
