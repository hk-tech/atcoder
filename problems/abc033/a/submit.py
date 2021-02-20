import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = input()

if N.count(N[0]) == 4:
    print('SAME')
else:
    print('DIFFERENT')




