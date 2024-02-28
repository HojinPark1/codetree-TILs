n=int(input())
for _ in range(n):
    k=input().split()
    a=int(k[0])
    b=int(k[1])
    sum_value=1
    for i in range(a, b+1):
        sum_value*=i
    print(sum_value)