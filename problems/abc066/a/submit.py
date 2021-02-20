import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

S = input()

for i in range(1, len(S)+1):
    s = S[:-i]
    c = Counter(s)
    keys = list(c.keys())
    if len(c) == 2 and c[keys[0]] == c[keys[1]]:
        print(len(S)-i)






