
        
amount=6000       
import random       
usrname=input("Enter your username:")
password=input("Enter your password:")

if usrname=="vaishu" and password=="1234":
    print("username and password verified✅")
    
    generatedOTP=random.randint(1000,9999)
    print("Your OTP is ",generatedOTP)
    
    otp=int(input("Enter your OTP:"))
        
    if otp==generatedOTP:
        print("=============welcome to Banking App===============")
        print("1.check balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")
        BankBalance=6000
        choice=int(input("Enter your choice:"))
        if choice==1:
            balance=6000
            print("Your balance is Rs",balance)
        elif choice==2:
            amount=int(input("Enter  deposit amount:"))
            if amount>0:
                BankBalance += amount
                print("deposit successful✅......\n after deposit your balance is Rs",BankBalance)
            else:
                print("Invalid amount")
        elif choice==3: 
            withdraw=int(input("Enter withdraw amount:"))
            if withdraw>0:
                if withdraw<=BankBalance:
                    BankBalance -= withdraw
                    print("withdraw successful✅......\n after withdraw your balance is Rs",BankBalance)
                else:
                    print("Insufficient balance❌")
            else:
                print("Invalid amount❌")           
        elif choice==4:
            print("Thank you for banking with us")           
    else:
        print("incorrect OTP❌")
    
else:
    print("incorrect username or password❌")
    