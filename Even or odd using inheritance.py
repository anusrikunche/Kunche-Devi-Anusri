class a:
    def __init__(self,data):
        self.data=data
    def even(self,n):
        if n%2==0:
            return "Even"
        else:
            return "Odd"
class b(a):
    def __init__(self,data1):
        self.data1=data1
        super().__init__(data1)
        print(self.even(self.data))
        print(self.odd(self.data))
    def odd(self,n):
        if n%2!=0:
            return "Odd"
        else:
            return "Even"
x=int(input())
obj=b(x)
