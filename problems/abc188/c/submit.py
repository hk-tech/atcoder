N = int(input())
A = list(map(int, input().split()))

num = 2 ** N
left_max = 0
right_max = 0
for i in range(0, num//2):
    if A[i] > left_max:
        left_max = A[i]
        left_i = i
    if A[i+num//2] > right_max:
        right_max = A[i+num//2]
        right_i = i+num//2

if left_max < right_max:
    print(left_i+1)
else:
    print(right_i+1)

    