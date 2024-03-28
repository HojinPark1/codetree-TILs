k=list(map(int, input().split()))
k2 = [0] * 10
for i in k:
    for j in range(1, 10):
        if j * 10 <= i < (j+1) * 10:
            k2[j] += 1

for i in range(1, 10):
    print(f"{i} - {k2[i]}")