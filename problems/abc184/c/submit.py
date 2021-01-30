r1, c1 = (int(i) for i in input().split())
r2, c2 = (int(i) for i in input().split())

r = r1 - r2
c = c1 - c2

if r == 0 and c == 0:
    print(0)
    exit()
elif abs(r) == abs(c):
    print(1)
    exit()
elif abs(r) + abs(c) <= 3:
    print(1)
    exit()
elif (r ^ c ^ 1) & 1:
    print(2)
    exit()
elif abs(r) + abs(c) <= 6:
    print(2)
    exit()
elif abs(r+c) <= 6 or abs(r-c) <= 6:
    print(2)
    exit()
else:
    print(3)
    exit()

