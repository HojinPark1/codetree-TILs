n=int(input())
k=list(map(int, input().split()))
k2=[0] * (10)
for elem in k:
    k2[elem] += 1

for i in range(1, 10):
    print(k2[i])