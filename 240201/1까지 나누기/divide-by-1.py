n=int(input())
k=1
for i in range(1, 5001):
    if n // i > 1:
        n=n//i
        k+=1
        continue
    elif n // i <= 1:
        print(k)
        break