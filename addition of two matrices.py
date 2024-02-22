#addition of two matrices
r,c=map(int,input().split())
l1,l2,l3=[],[],[0]*r
for i in range(r):
    l3[i]=[0]*c
for i in range(r):
    l1.append(tuple(map(int,input().split())))
print(l1)
for i in range(r):
    l2.append(tuple(map(int,input().split())))
print(l2)
for i in range(r):
    for j in range(c):
        l3[i][j]=l1[i][j]+l2[i][j]
for i in l3:
    print(i)
