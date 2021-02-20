import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
A = LI()

odds = 0
twos = 0
fours = 0

for a in A:
    if a % 4 == 0:
        fours += 1
    elif a % 2 == 0:
        twos += 1
    else:
        odds += 1

if odds - fours > 1:
    print('No')
elif odds - fours == 1:
    if twos == 0:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')
    
                


