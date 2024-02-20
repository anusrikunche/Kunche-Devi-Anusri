def armstrong(n,m):
    for i in range(n,m+1):
        x=i
        arm=0
        while i>0:
            d=i%10
            arm+=d**3
            i//=10
        if arm==x:
            print(x)
a,b=map(int,input().split())
armstrong(a,b)

        
        
