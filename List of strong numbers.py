def stronglist(n,m):
    for i in range(n,m+1):
        sum=0
        x=i
    while i>0:
        d=i%10
        fact=1
        for j in range(1,d+1):
            fact*=j
        sum+=fact
        i//=10
    if sum==x:
        print(x)
n,m=map(int,input().split())
stronglist(n,m)
