N, M = (int(i) for i in input().split())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
import sys;sys.setrecursionlimit(10**9)
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
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
 
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

u = UnionFind(N)
for _ in range(M):
    c, d = LI()
    u.union(c-1,d-1)

dic_a = {}
dic_b = {}
ok = True
for i in range(N):
    p = u.find(i)
    if p not in dic_a:
        dic_a[p] = A[i]
        dic_b[p] = B[i]
    else:
        dic_a[p] += A[i]
        dic_b[p] += B[i]

for k in dic_a.keys():
    if dic_a[k] != dic_b[k]:
        print('No')
        exit()
print('Yes')