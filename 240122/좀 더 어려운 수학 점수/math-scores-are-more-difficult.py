A=input().split()
a1=int(A[0])
a2=int(A[1])
B=input().split()
b1=int(B[0])
b2=int(B[1])

if a1>b1:
    print("A")
elif b1>a1:
    print("B")
elif a1==b1 and a2>b2:
    print("A")
elif a1==b1 and b2>a2:
    print("B")
else:
    pass