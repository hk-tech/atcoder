A, B, C = (int(i) for i in input().split())
P = {}
P[(99, 99, 99)] = 1

def f(a, b, c):
    a, b, c = sorted([a, b, c])
    if c == 100:
        return 0
    if (a, b, c) in P:
        return P[(a, b, c)]
    t = a + b + c
    ret = a/t * (f(a+1, b, c) + 1)
    ret += b/t * (f(a, b+1, c) + 1)
    ret += c/t * (f(a, b, c+1) + 1)
    P[(a,b,c)] = ret
    return ret 
    
print(f(A,B,C))