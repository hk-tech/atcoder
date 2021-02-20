import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

S = input()
N = len(S)
c = Counter(S)

if N == 2:
    print(1)
    exit()

if len(c) == 1:
    if N % 2 == 0:
        print(2)
    else:
        print(1)
    exit()

for i in range(1, N+1):
    s = S[:-i]
    if (N - i) % 2 == 1:
        continue
    else:
        if s[:(N-i)//2] == s[(N-i)//2:]:
            print(N-i)
            exit()








