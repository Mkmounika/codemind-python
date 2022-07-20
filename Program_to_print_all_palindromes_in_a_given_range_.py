l=int(input())
r=int(input())
sum=0
for i in range(l,r+1):
    num1=i
    num2=0
    while(num1!=0):
        rem=num1%10
        num2=num2*10+rem
        num1=num1//10
    if(i==num2):
        print(i,end=" ")
        