S=int(input())
A=int(input())
if S == 0:
    if A >= 19:
        print("MAN")
    elif A < 19:
        print("BOY")
elif S == 1:
    if A >= 19:
        print("WOMAN")
    else:
        print("GIRL")