n=int(input())
d={}
for i in range(n):
    name,number=map(str,input().split())
    d[name]=number
m=int(input("No.of search items:"))
for i in range(m):
    s=input()
    if s in d:
        print(s,"=",d[s])
    if s not in d:
        print("Not found")
