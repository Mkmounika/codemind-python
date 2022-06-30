import math
n=int(input())
a=list(map(int,input().split()))
m=0
n=0
for i in range(len(a)):
    if i%2==0:
        m=m+a[i]
    if i%2!=0:
        n=n+a[i]
print(n)