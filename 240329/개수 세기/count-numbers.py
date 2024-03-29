k=input().split()
n=int(k[0])
m=int(k[1])
cnt = 0
l=list(map(int, input().split()))
for i in range(n):
    if l[i] == m:
        cnt += 1
print(cnt)