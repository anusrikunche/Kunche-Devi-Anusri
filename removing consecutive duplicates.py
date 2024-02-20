s=input()
s1=""
for i in range(len(s)):
    if s[i-1]!=s[i]:
        s1+=s[i]
print(s1)
