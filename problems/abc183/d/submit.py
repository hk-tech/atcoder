N, W = (int(i) for i in input().split())

STP = [[int(i) for i in input().split()] for i in range(N)]
cum = [0] * (2 * (10 ** 5) + 1)

for s, t, p in STP:
    cum[s] += p
    cum[t] -= p

for i in range(1, len(cum)):
    cum[i] += cum[i-1]

if max(cum) > W:
    print('No')
else:
    print('Yes')