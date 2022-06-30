n=int(input())
rem=n%10
if rem==0:
    print(n//10)
if rem<0:
    print((n//10)-1)
if rem>0:
    print(n//10)