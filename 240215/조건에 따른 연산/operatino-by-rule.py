n=int(input())
k=0
while n < 1000:
    if n % 2 == 0:
        n = n * 3 + 1
        k+=1
    if n % 2 != 0:
        n = n*2 + 2
        k+=1
print(k)