l=list(map(str,input().split()))
c=0
d=[]
for i in l:
    c=0
    for j in i:
        if j in "AEIOUaeiou":
            c+=1
    d.append(c)
print(max(d))
            