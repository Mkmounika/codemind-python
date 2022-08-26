n=int(input())
a=list(map(int,input().split()))
s=0
l=0
for i in range(0,n):
    if(i%2!=0):
        s=s+a[i]
    if(i%2==0):
        l=l+a[i]
if(s-l==0):
    print("YES")
else:
    print("NO")
        
        
        
        
        
    