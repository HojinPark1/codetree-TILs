k=list(map(int, input().split()))
k2=[0]*7
for i in k:
    k2[i] += 1

for i in range(1, 7):
    print(f"{i} - {k2[i]}")