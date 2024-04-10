n1, n2 = tuple(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))

for i in range(n1):
    success = True
    for j in range(n2):
        if i + j >= n1:
            success = False
            print('No')
            break
        if A[i + j] != B[j]:
            success = False
            print('No')
            break
    if success:
        print("Yes")