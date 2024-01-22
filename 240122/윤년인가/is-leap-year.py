n=int(input())
if n%4==0 or (n%400==0):
    print("true")
elif n%100==0 and n%400!=0:
    print('false')
else:
    print('false')