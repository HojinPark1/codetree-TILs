n= int(input())
S=0
p=0
for i in range(1, 101):
    S += i
    if S >= n:
        p=i
        break
print(p)