X, K, D = (int(i) for i in input().split())

r = X // D
print(r)
if K % 2 == 0 and r % 2 == 0:
    print(abs(X - D * r))
elif K % 2 == 0 and r % 2 != 0:
    print(min(abs(X - D * (r+1)), abs(X - D * (r-1))))
elif K % 2 != 0 and r % 2 == 0:
    print(min(abs(X - D * (r+1)), abs(X - D * (r-1))))
else:
    print(abs(X - D * r))
