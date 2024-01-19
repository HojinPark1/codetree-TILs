n=int(input())
if n % 2 == 1:
    n = n + 3
if n % 3 == 0:
    n = int(n/3)

print(n)