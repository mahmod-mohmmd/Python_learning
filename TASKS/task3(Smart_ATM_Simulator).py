print("Welcom to you in my program")
PIN = int(input("Please enter your PIN:"))
Balance = 5000
if PIN == 1234 :
    process = input("Please enter your process(Withdraw (1) / Check Balance (2)): ")
    if process == "1" :
            withdraw = int(input("Please enter num you want to withdraw it")) 
            if withdraw > Balance :
                print("Sorry, your balance is insufficient.")
            else :
                print(f"The transaction was successful. Your remaining balance is: {Balance - withdraw}")
    elif process == "2" :
        print(f"Your Balance is {Balance}")
else :
    print("Incorrect PIN, transaction declined")
