k=list(map(int, input().split()))
a = k[0]
b = k[1]
ans=[0]*b
answer = 0

while a > 1:
    ans[a%b] += 1
    a = a//b
    if a <= 1:
        break

for i in range(b):
    ans[i] = ans[i] ** 2


for i in range(b):
    answer += ans[i]

print(answer)