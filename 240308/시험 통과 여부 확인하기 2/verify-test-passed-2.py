n=int(input())
p=0
for _ in range(n):
    S=0
    A=0
    k=list(map(int, input().split()))
    for j in range(4):
        S+=k[j]
        A+=1
    if S/A >= 60:
        print('pass')
        p+=1
    else:
        print('fail')
print(p)