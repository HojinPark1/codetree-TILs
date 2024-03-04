n = list(map(int, input().split()))
n_sum=0
n_num=0
for i in range(10):
    if n[i] < 250:
        n_sum+=int(n[i])
        n_num+=1
    else:
        print(f"{n_sum} {(n_sum/n_num):.1f}")
        break