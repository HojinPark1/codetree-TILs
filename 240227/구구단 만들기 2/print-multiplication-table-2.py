k=input().split()
a=int(k[0])
b=int(k[1])
for i in range(2, 9):
    if i % 2 == 0: 
            for j in range(b, a-1, -1):
                print(f"{j} * {i} = {j*i}", end=' ')
                if j > a:
                    print('/',end=' ')
            print()