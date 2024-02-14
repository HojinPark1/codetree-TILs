n=int(input())
t=0
while True:   
    if n == 1:
        print(t)
        break

    t+=1

    if n % 2 == 0:
        n = n // 2

    else:
        n = n * 3 + 1