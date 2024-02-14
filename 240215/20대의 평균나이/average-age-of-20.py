K=0
A=0
while True:
    a=int(input())
    if a < 20 or a >= 30:
        print(f"{K/A:.2f}") 
        break
    K+=a
    A+=1