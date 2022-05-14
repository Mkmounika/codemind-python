a=int(input())
for i in range(a):
    n=int(input())
    t=n
    r=0
    while n:
        rem=n%10
        r=r*10+rem
        n=n//10
    if(t==r):
        print(True)
    else:
        print(False)