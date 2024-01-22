P=input().split()
p1=P[0]
p2=int(P[1])
Q=input().split()
q1=Q[0]
q2=int(Q[1])
R=input().split()
r1=R[0]
r2=int(R[1])

if p1 == "Y" and q1 == "Y" and r1 == "N" :
    if p2 >= 37 and q2>=37:
        print("E")
    else:
        print("N")
elif p1 == "N" and q1 == "Y" and r1 == "Y":
    if q2 >= 37 and r2 >= 37:
        print("E")
    else:
        print("N")
elif p1 == "Y" and q1 == "N" and r1 == "Y":
    if p2 >= 37 and r2 >= 37:
        print("E")
    else:
        print("N")
elif p1 == "Y" and q1 == "Y" and r1 == "Y":
    if p2 <= 37 and q2 <= 37:
        print("N")
    elif p2 <= 37 and r2 <= 37:
        print("N")
    elif q2 <= 37 and r2 <= 37:
        print("N")
    else:
        print("E")