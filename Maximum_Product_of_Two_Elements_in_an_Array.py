a=list(map(int,input().split()))
max=0
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
         k=(a[i]-1)*(a[j]-1)
         if k>max:
                max=k
print(max)               
