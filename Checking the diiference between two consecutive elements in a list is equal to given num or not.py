n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(1,len(l)):
    if l[i]-l[i-1]==m:
        print("True")
    else:
        print("False")

