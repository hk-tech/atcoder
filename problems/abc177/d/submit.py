import sys;sys.setrecursionlimit(10**9)

N, M  = (int(i) for i in input().split())

def LI(): return [int(x) for x in sys.stdin.readline().split()]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

u = UnionFind(N)

for i in range(M):
    a, b = LI()
    u.union(a-1, b-1)

ans = 0

for i in range(N):
    ans = max(ans, u.size(i))

print(ans)