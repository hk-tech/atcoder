L = int(input())

import math

def combinations_count(n, r):
    if n <= 1:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(combinations_count(L-1, 11))

