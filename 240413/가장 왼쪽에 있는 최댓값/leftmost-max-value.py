n=int(input())
arr=list(map(int, input().split()))

while len(arr) > 1:
    if arr == []:
        break
    max_arr_index = arr.index(max(arr))
    arr = arr[0:max_arr_index]
    print(max_arr_index+1, end=' ')