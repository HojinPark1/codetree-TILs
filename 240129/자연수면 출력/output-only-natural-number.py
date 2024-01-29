n=input().split()
a=int(n[0])
b=int(n[1])
if a > 0:
    for _ in range(b):
        print(a, end='')
else:
    print("0")