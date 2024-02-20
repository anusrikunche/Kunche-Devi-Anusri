def strong(n):
    sum=0
    x=n
    while n>0:
        d=n%10
        fact=1
        for i in range(1,d+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        return "Strong number"
    else:
        return "Not a strong number"
n=int(input())
print(strong(n))
