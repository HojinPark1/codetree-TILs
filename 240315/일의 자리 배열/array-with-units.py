k=list(map(int, input().split()))
k2=list()
for _ in range(3, 11):
    k.append((k[-1]+k[-2])%10)

for i in range(10):
    print(k[i], end=' ')