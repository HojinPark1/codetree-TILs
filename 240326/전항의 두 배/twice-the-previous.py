k=list(map(int, input().split()))
for i in range(2, 11):
    k.append(k[i-1] + 2*k[i-2])

for i in range(10):
    print(k[i], end=' ')