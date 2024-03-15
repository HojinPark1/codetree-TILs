n=int(input())
arr=[0, 1]
arr[0]= 1
arr[1]= n
while arr[-1] < 100:
    arr.append(arr[-1] + arr[-2])

for i in range(len(arr)):
    print(arr[i], end=' ')