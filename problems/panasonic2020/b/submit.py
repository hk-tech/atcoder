import math
H, W = (int(i) for i in input().split())

odd = W // 2 if W % 2 == 0 else W // 2 + 1
even = W // 2

if H == 1 or W == 1:
    print(1)
else:
    if H % 2 == 0:
        print((odd+even)*(H//2))
    else:
        print((odd+even)*((H-1)//2)+odd)