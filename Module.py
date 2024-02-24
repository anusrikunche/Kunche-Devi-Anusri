def is_substring(s1,s2):
    if s2 in s1:
        print("Substring")
    else:
        print("Not a substring")
def substring(s):
    for i in range(1,len(s)+1):
        print(s[:i])
        
