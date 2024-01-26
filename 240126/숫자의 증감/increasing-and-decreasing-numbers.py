P=input().split()
c=P[0]
n=int(P[1])
if c == "A":
    for i in range(1, n+1):
        print(i, end = ' ')
elif c == "D":
    k = n
    while k >=1:
        print(k, end = ' ')
        k-=1