S = input()

prev = 'xxx'
ans = ''
for s in S:
    if s != ' ':
        ans += s
    else:
        if prev != ' ':
            ans += ','
    prev = s

print(ans)

