S = input()
k = len(S)
ans = 10 ** 10
for mask in range(2 ** k):
    total = 0
    cnt = k
    for i in range(k): 
        if (mask >> i) & 1:
            total += int(S[i])
            cnt -= 1

    if total % 3 == 0 and total > 0:  
        ans = min(ans, cnt)

if ans == 10 ** 10:
    print('-1')
    exit()
print(ans)


