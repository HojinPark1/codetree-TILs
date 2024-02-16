Sat = True
for _ in range(5):
    K=int(input())
    if K % 3 != 0:
        Sat = False
if Sat == True:
    print("1")
else:
    print("0")