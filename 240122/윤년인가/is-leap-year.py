n=int(input())
if n%4==0:
    if n%100==0:
        if n%400==0:
            print('true')
        elif n%400!=0:
            print('false')
    else:
        print('true')
else:print('false')