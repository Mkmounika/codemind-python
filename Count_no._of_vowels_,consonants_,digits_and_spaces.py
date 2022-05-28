a=input()
c=0
v=0
s=0
d=0
for i in range(len(a)):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
        v+=1
    elif(a[i]==' '):
        s+=1
    elif(a[i]>='0' and a[i]<='9'):
        d+=1
    else:
        c+=1
print('Vowels: %d'%v)
print('Consonants: %d'%c)
print('Digits: %d'%d)
print('White spaces: %d'%s)