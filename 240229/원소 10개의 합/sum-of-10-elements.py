n=list(map(int, input().split()))
ans=0
for i in range(10):
    ans += n[i]
print(ans)