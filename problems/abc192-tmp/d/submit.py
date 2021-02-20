import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

X = input()
M = int(input())

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

d = int(max(X))
ans = 0
bef = 10 ** 18 + 1

if M >= 10 ** 5:
    print(M - Base_n_to_10(d+1) + 1)

for i in range(d+1, 10 ** 18):
    num = Base_n_to_10(X, i)
    #print(i, num)
    if bef == num:
        print(ans)
        exit()
    if num <= M:
        ans += 1
    else:
        print(ans)
        exit()
    bef = num

print(0)




