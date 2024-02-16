Sat = True
K=input().split()
a=int(K[0])
b=int(K[1])
c=int(K[2])
for i in range(a, b+1):
    if i % c == 0:
        Sat = False
if Sat == False:
    print("NO")
else:
    print("YES")