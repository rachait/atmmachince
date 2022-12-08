h="WELCOME TO ATM"
print(h.center(30))
n=input("Enter account name:")
print("Hello",n,"Your Account Number is:123456789")
amt=5000
c="yes"
while c=="yes":
    print("1.WITHDRAW")
    print("2.DEPOSIT")
    print("3.BALANCE")
    choice=int(input("Enter your choice:"))
    if choice==1:
       w=int(input("Enter the amount:"))
       s=amt-w
       if w>amt:
          print("Insufficient fund")
       else:
           print("Amount withdrawed is:",w)
           amt=s
       if amt<5000:
        print("low balance")
    if choice==2:
       ad=int(input("Enter amount to deposit:"))
       j=amt+ad
       print("Amount deposited is:",ad)
       print("balance amount is:",j)
       amt=j
    if choice==3:
        print("Available Balance is:",amt)
        if amt<5000:
           print("low balance")  
    c=input("do you wnat continue yes/no:")
else:
    f=("THANKYOU")
    print(f.center(30))
