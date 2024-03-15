n=int(input())
k=list(map(int, input().split()))
k2 =[k[elem] ** 2 for elem in range(n)]

for i in range(n):
    print(k2[i], end=' ')