n=int(input())
temp=n
arm=0
while n>0:
    digit=n%10
    arm+=digit**3
    n//=10
if temp==arm:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
