n=int(input())
Sat=False
for i in range(2, 501):
    if n % i == 0:
        Sat=True

if Sat==True:
    print("C")
else:
    print("N")