n=int(input())
arr=list(map(float, input().split()))
G_S=0
G_A=0
G="Ungraded"
for i in range(n):
    G_S+=arr[i]
    G_A+=1
if G_S/G_A >= 4.0:
    G="Perfect"
elif 4>G_S/G_A>= 3.0:
    G="Good"
else:
    G="Poor"
print(f"{G_S/G_A:.1f}")
print(G)