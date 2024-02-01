n=input().split()
a=int(n[0])
b=int(n[1])
k=1
for i in range (1, b+1):
    if i % a == 0:
        k *= i
print(k)