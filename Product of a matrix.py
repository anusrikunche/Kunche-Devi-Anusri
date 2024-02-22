#product of a matrix
r,c=int(input("Rows:")),int(input("Columns:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
prod=1
for i in l:
    print(i)
    for j in i:
        prod*=j
print(prod)
