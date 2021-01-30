a, b, x, y = (int(i) for i in input().split())

if a > b:
    print(min((a-b-1)*y+x, (a-b-1)*2*x+x))
elif a < b:
    print(min((b-a)*y+x, (b-a)*2*x+x))
else:
    print(x)