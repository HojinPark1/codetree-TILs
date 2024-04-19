n=4

arr=[
    list(map(int, input().split()))
    for _ in range(n)
]
for i in range(n):
    sum_arr=0
    for j in range(n):
        sum_arr += arr[i][j]
    print(sum_arr)