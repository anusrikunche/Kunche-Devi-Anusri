def armstrong(m,n):
    for i in range(m,n+1):
        x=str(i)
        arm=0
        for j in x:
            arm+=int(j)**len(x)
            i//=10
        if str(arm)==x:
            print(x)
m,n=map(int,input().split())
armstrong(m,n)
    
