n = int(input())
x = 0
while True:
    if n > 1:
        n //= 2
        x += 1
    else:
        break
print(x)