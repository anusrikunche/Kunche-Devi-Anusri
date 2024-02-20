n,m=map(int,input().split())
i=n
while i<=m:
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
    i+=1
