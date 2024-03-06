rr=list(map(int, input().split()))
S=0
N=0
A=0
for i in range(10):
    if rr[i] != 0:
        S+=rr[i]
        N+=1
    else:
        break
print(f"{S} {S/N:.1f}")