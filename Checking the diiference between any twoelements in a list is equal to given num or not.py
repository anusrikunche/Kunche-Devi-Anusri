n,m=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in range(n):
    for j in range(n):
        if l[i]-l[j]==m:
            flag=1
x=True if flag==1 else False
print(x)
