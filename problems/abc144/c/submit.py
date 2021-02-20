import sys, math, itertools
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**9)
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
 
    divisors.sort()
    return divisors

d = make_divisors(N)
n = len(d)

ans = 10 ** 12
for i in range(n//2+1):
    ans = min(ans, d[i]-1 + N//d[i]-1)

print(ans)


