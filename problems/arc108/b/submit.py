N = int(input())
S = input()

#S = 'fofofoxfofoxtfofoxxxxx'
#N = len(S)

lis = []
ans = 0
F = 'fox'

for s in S:
    lis.append(s)

    if len(lis) >= 3:
        ok = True
        for i in range(3):
            if lis[-i-1] != F[-i-1]:
                ok = False
        
        if ok:
            del lis[-3:]
            ans += 3

print(N - ans)


    
