def encryption(s,key):
    se=""
    for i in s:
        e=ord(i)+key
        se+=chr(e)
    return se
def decryption(s,key):
    sd=""
    for j in s:
        d=ord(j)-key
        sd+=chr(d)
    return sd
s=input()
key=int(input())
a=input()
if a=="encryption":
    print(encryption(s,key))
elif a=="decryption":
    print(decryption(s,key))
else:
    print("Improper operation")
