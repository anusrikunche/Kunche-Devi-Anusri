def palindrome(n,l):
    x=str(n)
    s=x[::-1]
    if int(s)==n and n%2==0:
        l.append(n)
a,b=map(int,input().split())
l=[]
for i in range(a,b+1):
    palindrome(i,l)
print(l)
print(sum(l))


