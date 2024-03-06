arr=list(map(float, input().split()))
S_G=0
S_A=0
A=0
for i in range(8):
    S_G+=arr[i]
    S_A+=1
print(f"{S_G/S_A:.1f}")