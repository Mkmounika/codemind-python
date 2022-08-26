n=int(input())
a=list(map(int,input().split()))
d=[]
m=0
c=0
for i in range(n):
    if(a[i]==1):
        c+=1
        if c>m:
            m=c
    else:
        c=0
print(m)

