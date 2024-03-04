n = list(map(int, input().split()))
n_sum=0
n_num=0
n2_sum=0
n2=list()
for i in range(10):
    if n[i] < 250:
        n2.append(n[i])
        n_num+=1
    else:
        break

for j in range(len(n2)):
    n2_sum+=n2[j]
print(f"{n2_sum} {n2_sum/n_num:.1f}")