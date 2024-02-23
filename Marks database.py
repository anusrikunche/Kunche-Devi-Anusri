#Write a python program to maintain students marks database using nested dictionary
n,m=map(int,(input().split()))
d={}
for i in range(n):
    k=input("Enter roll number: ")
    d1={}
    v=d1
    for j in range(m):
        k1=input("Enter Subject: ")
        v1=input("Enter marks:")
        d1[k1]=v1
    d[k]=v
for i in d:
    print(i,"=",d[i])
