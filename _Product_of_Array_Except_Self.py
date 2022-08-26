n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    pro=1
    for j in range(n):
        if (i!=j):
            pro=pro*a[j]
    print(pro,end=' ')