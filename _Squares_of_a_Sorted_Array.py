n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    l.append(i*i)
    l.sort()
print(*l)