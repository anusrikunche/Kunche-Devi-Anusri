"""discount for men:5%
discount for women:7%
discount on each item:3*No of items purchased
calculate total bill.
Take items and their prices in runtime"""
m=int(input("Enter no. of items purchase:"))
g=input("Enter gender of the customer:")
dis=3*m
d={}
l=[]
for i in range(m):
    k=input("Item: ")
    v=int(input("Price: "))
    d[k]=v
print(d)
for i in d:
    l.append(d[i]-(dis*d[i])/100)
if g=="male":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items-prices:discount-prices")
for i in d:
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"Total bill:{bill}")
