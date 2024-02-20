p=int(input())
count=0
for i in range(1,p):
    if p%i==0:
        print(i)
        count+=i
if count==p:
    print("Perfect number")
else:
    print("Not a perfect number")
