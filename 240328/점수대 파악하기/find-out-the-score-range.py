k=list(map(int, input().split()))
k2 = [0] * 11
for i in k:
    if i == 0:
        break
    for j in range(1, 11):
        if j* 10 <= i < (j+1) * 10:
            k2[j] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {k2[i]}")