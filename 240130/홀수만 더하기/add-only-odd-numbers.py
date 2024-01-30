n=int(input())
K=0
for _ in range(n):
    i=int(input())
    if i % 2 == 1 and i % 3 == 0:
        K += i
print(K)