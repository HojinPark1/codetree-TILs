n=input().split()
a=int(n[0])
b=int(n[1])
K=0
if b >= a:
    for i in range(a,b+1):
        if i % 5 == 0:
            K += i
elif a >= b:
    for i in range(b, a+1):
        if i % 5 == 0:
            K += i
print(K)