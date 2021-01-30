A, B = (i for i in input().split())

sumA = 0
sumB = 0

for a in A:
    sumA += int(a)

for b in B:
    sumB += int(b)

print(max(sumA, sumB))