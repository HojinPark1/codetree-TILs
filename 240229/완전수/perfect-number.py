n=input().split()
start=int(n[0])
end=int(n[1])
ans=0
for i in range(start, end+1):
    cnt=0
    for j in range(1, i):
        if i % j == 0:
            cnt+=j
    if cnt == i:
        ans+=1
print(ans)