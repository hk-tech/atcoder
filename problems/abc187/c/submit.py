N = int(input())
S = []
for _ in range(N):
    S.append(input())

S = set(S)
newS = []
for s in S:
    if '!' in s:
        newS.append(s[1:])
        if s[1:] in S:
            out = s[1:]
    else:
        newS.append(s)

if len(set(S)) == len(set(newS)):
    print('satisfiable')
else:
    print(out)


