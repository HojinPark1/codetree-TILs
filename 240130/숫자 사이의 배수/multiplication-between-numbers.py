n=input().split()
a=int(n[0])
b=int(n[1])
S = 0
A = 0
M = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        S = S+i 
        A = A+i
        M +=1
A = round(A/M, 1)
print(S, A)