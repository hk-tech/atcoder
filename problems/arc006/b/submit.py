N, L = (int(i) for i in input().split())

lis = list(range(N))

for i in range(L):
    amida = input()
    for j, x in enumerate(amida):
        if j % 2 != 0 and x == '-':
            tmp = lis[j//2]
            lis[j//2] = lis[j//2 + 1]
            lis[j//2 + 1] = tmp

goal = input()
pos = goal.find('o')//2
#print(pos, lis)
print(lis[pos]+1)