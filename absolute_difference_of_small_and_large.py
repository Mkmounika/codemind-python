l=list(map(str,input().split()))
d=[]
for i in l:
    d.append(abs(ord(min(i))-ord(max(i))))
for i in d:
    print(i,end=' ')
    