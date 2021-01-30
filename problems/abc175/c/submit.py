import numpy as np
X, K, D = (int(i) for i in input().split())
X = abs(X)

if X - D * K > 0:
    print(X - D * K)
else:
    print(abs(X % D - D * (((X // D % 2) ^ (K % 2)) % 2)))