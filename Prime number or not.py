p=int(input())
count=0
for i in range(1,p+1):
    if p%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not a Prime number")
        
