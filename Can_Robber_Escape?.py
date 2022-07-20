x=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(x):
    if(arr[i]%2!=0):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")
    
    