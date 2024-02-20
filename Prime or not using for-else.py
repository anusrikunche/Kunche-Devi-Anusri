p=int(input())
count=0
for i in range(2,p):
    if p%i==0:
        print("Not a prime")
        break
else:
    print("Prime number")
