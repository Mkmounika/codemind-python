a,b=map(int,input().split())
if a>b:
    a,b=b,a
c=b
while True:
    if c%a==0 and c%b==0:
        print(c)
        break
    c+=1