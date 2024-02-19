a,b,c,d=map(int,input().split(" "))
fa=a-(a*c/100)
fb=b-(b*d/100)
if fa==fb:
    print("Any")
else:
    if fa<fb:
        print("First")
    else:
        print("Second")
