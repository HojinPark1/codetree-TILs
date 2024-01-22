N1=input().split()
a1=int(N1[0])
a2=N1[1]
N2=input().split()
b1=int(N2[0])
b2=N2[1]
if (a1 >= 19 and a2 == "M") or (b1>=19 and b2 == "M"):
    print("1")
else:
    print("0")