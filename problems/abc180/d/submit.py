X, Y, A, B = (int(i) for i in input().split())

ans = 0
while X * A < X + B and X < Y:
    X *= A
    ans += 1

print(ans + (Y - X - 1) // B)

