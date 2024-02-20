n,m=map(int,input().split())
for i in range(n,m+1):
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
