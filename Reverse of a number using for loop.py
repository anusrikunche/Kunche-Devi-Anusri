n=int(input())
sum=0
for i in range(n):
    if n>0:
        digit=n%10
        sum=digit+sum*10
        n//=10
print(sum)
    
