class Anu:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)
obj=Anu()
obj.fact(int(input()))
