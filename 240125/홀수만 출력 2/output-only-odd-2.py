n=input().split()
a=int(n[0])
b=int(n[1])
for i in range(a+1, b-1, -1):
    if i % 2 == 1:
        print(i, end = ' ')