n=input().split()
a=int(n[0])
b=int(n[1])
if a<90:
    print("0")
elif a>=90 and b<90:
    print("0")
elif a>=90 and b>=90 and b<95:
    print("50000")
elif a>=90 and b>=95:
    print("100000")