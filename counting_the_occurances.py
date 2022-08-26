Astr=input()
char=input()
c=0
for i in range(len(Astr)):
    if(char==Astr[i]):
        c+=1
if(c==0):
    print(-1)
else:
    print(c)
    