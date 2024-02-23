def isprime(a):
    for i in range(2,a):
        if a%i==0:
            return "Composite"
    else:
        return "Prime"
n=int(input())
d={}
for i in range(1,n+1):
    k=i
    v=isprime(i)
    d[k]=v
print(d)
    
