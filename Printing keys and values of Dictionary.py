n=int(input())
d={}
for i in range(n):
    key=input("Key: ")
    value=input("Value: ")
    d[key]=value
print(d)
#using comma
for i in d:
    print("key: ",i," ","value: ",d[i])
#using builtin functions
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
#using f function
for i in d:
    print(f"Key:{i} value:{d[i]}")
#using format function
for i in d:
    print("key:{} value:{}".format(i,d[i]))
