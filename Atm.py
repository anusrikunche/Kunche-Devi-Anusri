x,y=map(int,input().split(" "))
if x>y:
    print("Insufficient balance")
else:
    if x<y and x%5==0:
        print("Transaction is successful and remained balance is",y-x)
    else:
        print("Incorrect Withdrawl Amount(not multiple of 5)")
