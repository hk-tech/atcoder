import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

S = input()

d = 'WBWBWWBWBWBW'
full = d * 3

lis = ['Do','Do', 'Re', 'Re','Mi','Fa', 'Fa','So', 'So','La', 'La', 'Si']
for i in range(len(full)-19):
    if S == full[i:i+20]:
        print(lis[i%len(lis)])
        exit()





