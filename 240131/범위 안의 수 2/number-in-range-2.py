i = 0
k=0
for _ in range(10):
    n=int(input())
    if n > 200 or n < 0:
        pass
    else:
        i += n
        k += 1
print(i, round(i/k, 1))