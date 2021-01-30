import numpy as np
import math

N, M = (int(i) for i in input().split())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(N+1)
A.sort()

diffA = np.diff(A) - 1
diffA = diffA[diffA > 0]

if M == 0:
    print(1)
    exit()
elif len(diffA) == 0:
    print(0)
    exit()

k = min(diffA)
ans = 0
for x in diffA:
    ans += math.ceil(x/k)

print(ans)