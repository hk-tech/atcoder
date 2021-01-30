N, H, W = (int(i) for i in input().split())
import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]

ans = 0
for i in range(N):
    a, b = LI()
    if a >= H and b >= W:
        ans += 1

print(ans)




