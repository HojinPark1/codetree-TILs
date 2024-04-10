n1, n2 = map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

ans = True

for i in range(n1):
    for j in range(n2):
        if i + j >= n1:
            ans = False
            break
        if A[i + j] != B[j]:
            ans = False
            break
        else:
            ans = True
            break
    if ans = True:
        break

if ans == True:
    print('Yes')
else:
    print('No')