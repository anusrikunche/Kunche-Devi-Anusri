s=input()
ce=0
co=0
for i in range(0,len(s),2):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='0' or s[i]=='u':
        ce+=1
print("Even",ce)
for i in range(1,len(s),2):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='0' or s[i]=='u':
        co+=1
print("odd",co)
    
