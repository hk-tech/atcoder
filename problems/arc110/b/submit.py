import math
N = int(input())
T = input()

s = '110'

if T == '1':
    print(2 * (10 ** 10))
elif T == '0':
    print(10 ** 10)
else:
    if T[:2] == '10':
        T = '1' + T
    elif T[:2] == '01':
        T = '11' + T

    N = len(T)
    for i in range(N):
        if T[i] != s[i%3]:
            print(0)
            exit() 
    print(10 ** 10 - (N-1)//3)

# 難しかった