arr=list(map(int, input().split()))
arr_r=list()
for i in range(10):
    if arr[i] != 0:
        arr_r.append(arr[i])
    if arr[i] == 0:
        break
arr_r = arr_r[::-1]
for i in range(len(arr_r)):
    print(arr_r[i], end=' ')