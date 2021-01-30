from functools import reduce
from operator import xor
N = int(input())
A = list(map(int, input().split()))

S = reduce(xor, A)
ans = []

for a in A:
    ans.append(S^a)

print(*ans)