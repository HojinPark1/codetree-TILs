n=int(input())
for _ in range(n):
    k=input().split()
    a=int(k[0])
    b=int(k[1])
    ans=0
    for i in range(a, b+1):
        if i % 2 == 0:
            ans+=i
    print(ans)