n=int(input())
K=1
P=0
for i in range(1, 11):
    K *= i
    if K >= n:
        P = i
        break
print(P)