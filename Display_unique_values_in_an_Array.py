n=int(input())
a=list(map(int,input().split()))
b=[]
l=0
c=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if(a[i]==a[j] and i!=j):
            c+=1
    if(c==0):
        b.append(a[i])
        l+=1
if(l!=0):
    print(*b)
else:
    print("-1")



