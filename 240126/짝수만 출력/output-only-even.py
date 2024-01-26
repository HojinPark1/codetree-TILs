n=input().split()
a=int(n[0])
b=int(n[1])
i = a
while i <= b:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1