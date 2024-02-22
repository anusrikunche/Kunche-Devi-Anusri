#sum of max and min value in a matrix using tuple
r,c=int(input("Rows:")),int(input("Columns:"))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(max+min)
