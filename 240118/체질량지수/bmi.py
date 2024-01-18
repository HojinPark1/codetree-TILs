#BMI = Kg / m**2
n=input().split()
h=int(n[0])
m=int(n[1])
O=int(m // (h**2/10000))
print(O)
if O >= 25:
    print("Obesity")