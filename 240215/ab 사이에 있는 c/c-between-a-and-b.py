K=input().split()
a=int(K[0])
b=int(K[1])
c=int(K[2])
Sat=False
for i in range(a, b+1):
    if i % c == 0:
        Sat=True
if Sat==True:
    print("YES")
else:
    print("NO")