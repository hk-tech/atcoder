import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

a, b, c = LI()

from decimal import Decimal

if c - a - b < 0:
    print('No')
else:
    if pow(c-a-b, 2) > 4 * a * b:
        print('Yes')
    else:
        print('No')