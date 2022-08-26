n=int(input())
a=list(map(int,input().split()))
b=int(input())
k=max(a)
for i in range(len(a)):
    if a[i]+b<k:
        print("False",end=' ')
    else:
        print("True",end=' ')
    