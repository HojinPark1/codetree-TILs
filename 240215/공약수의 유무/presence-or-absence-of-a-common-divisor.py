K=input().split()
Sat=False
a=int(K[0])
b=int(K[1])
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        Sat=True
if Sat == True:
    print("1")
else:
    print("0")