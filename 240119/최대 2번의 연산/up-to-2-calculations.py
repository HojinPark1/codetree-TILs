n=int(input())

if n % 2 == 0:
    n = int(n/2)

if n % 2 == 1:
    n = int((n+1)/2)

print(n)