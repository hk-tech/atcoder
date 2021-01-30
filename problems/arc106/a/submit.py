N = int(input())

for a in range(1, 40):
    for b in range(1, 28):
        if 3 ** a + 5 ** b == N:
            print(a, b)
            exit()

print(-1)