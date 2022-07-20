store=list(map(int,input().split()))
count=0
for i in range(store[0],store[1]+1):
    if(i%store[2]==0):
        count+=1
print(count)