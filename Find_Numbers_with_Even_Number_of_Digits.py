def digit(i):
    c=0
    k=0
    while(i>0):
        d=i%10
        c+=1
        i=i//10
    if c%2==0:
        k+=1
    return k
n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    d.append(digit(i))
m=sum(d)
print(m)
    