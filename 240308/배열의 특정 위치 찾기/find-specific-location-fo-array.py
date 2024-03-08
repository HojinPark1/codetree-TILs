k=list(map(int, input().split()))
s=0
n=0
m=0
for i in range(10):
    if (i+1) % 2 == 0:
        s+=k[i]
    if (i+1) % 3 == 0:
        n+=k[i]
        m+=1
print(f"{s} {n/m:.1f}")