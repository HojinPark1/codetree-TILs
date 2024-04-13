arr = list(map(int, input().split()))
arr2= []

for i in arr:
    if i == 999 or i == -999:
        break
    else:
        arr2.append(i)

print(max(arr2), min(arr2), end=' ')