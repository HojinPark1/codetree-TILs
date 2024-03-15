n=int(input())
arr=list()
tmp=0
for i in range(1, 11):
    arr.append(n*i)

for i in range(10):
    if arr[i] % 5 == 0:
        tmp+=1
        print(arr[i], end=' ')
        if tmp == 2:
            break
    else:
        print(arr[i], end=' ')