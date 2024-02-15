n=int(input())
k=0
while True:
    if n < 1000:
        if n % 2 == 0:
            n = n * 3 + 1
            k+=1
        elif n % 2 == 1:
            n = n*2 + 2
            k+=1
    else:
        break
print(k)