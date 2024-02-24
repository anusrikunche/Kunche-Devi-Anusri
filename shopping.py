"""discount for men:5%
discount for women:7%
discount on each item:3*No of items purchased
calculate total bill.
Take items and their prices in runtime"""
m=int(input("Enter no. of items purchase:"))
s=input("Enter gender of the customer:")
dis=3*m
d={}
l1=[]
for i in range(m):
    k=input("Item: ")
    v=int(input("Price: "))
    d[k]=v
print(d)
if s=="male":
    for i in d:
        d[i]=d[i]-(dis)+(5*(d[i]))/100
        l1.append(d[i])
    print(l1)
    print("Total bill=",sum(l1))
elif s=="female":
    for i in d:
        d[i]=d[i]-(dis)+((7*(d[i]))/100)
        l1.append(d[i])
    print("Total bill=",sum(l1))
else:
    print("None")


