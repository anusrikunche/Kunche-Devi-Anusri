class string:
    def length(self,s):
        print("Length :",len(s))
class A:
    def Characters(self,s):
        v,c=[],[]
        for i in s:
            if i.lower() in "aeiou":
                v.append(i)
            else:
                c.append(i)
        print("Vowels:",v,"\nConsonents:",c)
class B:
    def count(self,s):
        for i in s:
            print(i,"Count:",s.count(i))
class C(string,A,B):
    def __init__(self,data):
        self.data=data
        self.length(data)
        self.Characters(data)
        self.count(data)
        print("Completed")
x=input()
obj=C(x)
