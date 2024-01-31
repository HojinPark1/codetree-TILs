n=int(input())
o=0
p=0
for _ in range(n):
    m=int(input())
    o+=m
    p+=1
print(o, round(o/p, 1))