#testcase:Post Stop
s1,s2=map(str,input().split())
c,d=s1.lower(),s2.lower()
if len(s1)==len(s2):
    if set(c)==set(d):
        print("True")
    else:
        print("False")
else:
    print("False")
