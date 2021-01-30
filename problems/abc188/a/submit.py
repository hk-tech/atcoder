X, Y= (int(i) for i in input().split())

if min(X, Y) + 3 > max(X, Y):
    print('Yes')
else:
    print('No')