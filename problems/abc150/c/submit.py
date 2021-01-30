import itertools
N = int(input())
P = list(map(str, input().split()))
Q = list(map(str, input().split()))

p = ''.join(P)
q = ''.join(Q)

if p == q:
    print(0)
    exit()
i = 1
for x in itertools.permutations(range(1, N+1)):
    x = list(map(str, x))
    arr = ''.join(x)
    if p == arr:
        a = i
    if q == arr:
        b = i
    i += 1

print(abs(a-b))