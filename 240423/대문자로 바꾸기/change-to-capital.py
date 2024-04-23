n=5

arr=[ 
    list(map(str, input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(3):
        arr[i][j] = chr(ord(arr[i][j]) + ord('A') - ord('a'))
        print(arr[i][j], end=' ')
    print()