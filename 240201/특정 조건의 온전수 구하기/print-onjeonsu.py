n=int(input())
k=0
for i in range(1, n+1):
    if i % 2 == 0:
        continue
    elif i % 5 == 0:
        continue
    elif i % 3 == 0 and i % 9 != 0:
        continue
    print(i, end=' ')