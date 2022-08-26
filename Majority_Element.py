n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        if l[i]==l[j]:
            s+=1
    if s>n//2:
        print(l[i])
        break