N, A, B = (int(i) for i in input().split())

X = min(N, 5)
print(X * B + (N-X) * A)

