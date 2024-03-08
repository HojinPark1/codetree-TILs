k=list(map(int, input().split()))
s=0
n=0
for i in range(10):
    if (i+1) % 2 == 0:
        s += k[i]
    if (i+1) % 2 != 0:
        n += k[i]

if s > n:
    print(s - n)
else:
    print(n-s)