n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==0:
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in range(len(a)):
    print(a[i],end=' ')

            
        
        
        
        
        
        
        
        
        
        
