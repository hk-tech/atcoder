import math
A, B = (int(i) for i in input().split())

for i in range(1, 2 * 10 ** 4):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        print(i)
        exit()

print('-1')