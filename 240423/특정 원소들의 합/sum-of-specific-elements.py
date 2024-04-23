arr=[
    list(map(int, input().split()))
    for _ in range(4)
]

ans=0

for i in range(4):
    if i == 0:
        for j in range(1):
            ans += arr[i][j]
    if i == 1:
        for j in range(2):
            ans += arr[i][j]
    if i == 2:
        for j in range(3):
            ans += arr[i][j]
    if i == 3:
        for j in range(4):
            ans += arr[i][j]

print(ans)