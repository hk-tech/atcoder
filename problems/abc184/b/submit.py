N, X = (int(i) for i in input().split())
S = input()

ans = X
for s in S:
    if s == "o":
        ans += 1
    if s == "x" and ans > 0:
        ans -= 1

print(ans)
