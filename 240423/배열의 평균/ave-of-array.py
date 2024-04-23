arr=[
    list(map(int, input().split()))
    for _ in range(2)
]

arr_a = 0

for i in range(2):
    arr_w = 0
    for j in range(4):
        arr_w += arr[i][j]
    print(f"{arr_w/4:.1f}", end=' ')
print()

for i in range(4):
    arr_l = 0 
    for j in range(2):
        arr_l += arr[j][i]
    print(f"{arr_l/2:.1f}", end=' ')
print()

for i in range(2):
    for j in range(4):
        arr_a += arr[i][j]
print(f"{arr_a/8:.1f}")