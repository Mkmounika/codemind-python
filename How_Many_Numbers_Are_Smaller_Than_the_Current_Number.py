n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    s=0
    for j in range(len(a)):
        if(a[i]>a[j]):
            s+=1
    print(s,end=' ')


