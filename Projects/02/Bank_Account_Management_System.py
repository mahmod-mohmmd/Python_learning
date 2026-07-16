def main():
    while True :
            print("1️⃣  Enter To Program")
            print("2️⃣  Exit")
            choice = input("Choice (1/2): ")
            if choice == "1":
                numOfUsers = input("Are you want to know number of users?(y/n): ")
                if numOfUsers in("y" , "Y"):
                    print(f"The Number of users in our Bank is: {len(users)}.")
                mainManue()
            elif choice == "2":
                print("GoodBye 👋")
                break
            else:
                print("❌Invalid choice, try again‼️")
                
def mainManue():
        while True:
            print("=============================================")
            print("========== Welcom To Python Bank ============")
            print("=============================================")
            print("1️⃣  Register")
            print("2️⃣  Login")
            print("3️⃣  Exit")
            choice = input("Choice (1/2/3): ")
            if choice == "1" :
                Register()

            elif choice == "2":
                if Login() == True:
                    bankMenue()
                
            elif choice == "3" :
                print("You Chose Exit")
                break
            else :
                print("❌Invalid choice, try again‼️")
                
def bankMenue():         
    print(f"--------------------------------\nYour Balance is: {users[userName]["Balance"]} EGP💸")
    while True :
        print("================================")
        print("========== Bank Menue ==========")
        print("================================")
        print("1️⃣  Check Balance")
        print("2️⃣  Deposit💸")
        print("3️⃣  Withdraw💸")
        print("4️⃣  Transfer💱")
        print("5️⃣  Change Password")         
        print("6️⃣  Change User Name")
        print("7️⃣  Logout")
        print("8️⃣  Show Last Transacion")
        print("9️⃣  Main Menue")
        
        choice = input("Choice (1/2/3/4/5/6/7/8/9): ")
        if choice == "1":
            checkBalance()
        elif choice == '2':
            deposit() 
        elif choice == '3':
            withdraw() 
        elif choice == '4':
            transfer() 
        elif choice == '5':
            changePassword() 
        elif choice == '6':
            changeUsername() 
        elif choice == '7': 
            logout() 
            break
        elif choice == '8': 
            showLastTransaction() 
        elif choice == '9': 
            mainManue() 
        else :
            print("❌Invalid choice, try again‼️")
            
            
def showLastTransaction():
    print(users[userName]["lastTransaction"])
    
def printReceipt(transacionType , amount , recipient = ""):
    
    print("================================================")
    print(f"------------------🏦 Receipt🧾------------------")
    # print("--------- Python Bank 🏦 ---------")
    print("================================================")
    print(f"Current User Name : {userName}")
    print(f"Transacion Type   : {transacionType}")
    print(f"The Amount used   : {amount} EGP💸")
    if recipient != "":
        print(f"Transfered To : {recipient}")
    
    print(f"Remaining Balance : {users[userName]["Balance"]} EGP💸")
    print("===============================================")
    print("     ❤️  Thank You For Using Our Bank 🏦     ")
    print("===============================================\n")
    
users = {}
userName = ""
def Register():
    global userName
    print("You In Register.")
        
    userName = input("Please Enter Your Name: ").strip().capitalize()
    
    while userName in users   :
        print("User Name Exists‼️")
        userName = input("Please Enter Another Name: ").strip().capitalize()
    
    password = (input("Please Enter Your Password: "))
    
    while len(password) < 6  or password == "" :
        print("❌Password invalid,Password Must be AtLeast 6‼️")
        password = (input("Enter Your Password Again:  "))
        
    users[userName] = {}
    users[userName] = {"Password" : password , "Balance" : 0, "lastTransaction":"No Transaction yet"}
    
    print("Registration Successfull✅")
    print(f"Now The Number of users in our Bank Is: {len(users)}")
    print("Go To The Main Menue...") 
    return

def Login() :
    global userName
    print("You In Login.")
    attempts = 3 
    while(attempts > 0 ):
        userName = input("Please Enter Your Name: ").strip().capitalize()
        password = str(input("Please Enter Your Password: "))
    
        if (((userName not in users) or (users[userName]["Password"] != password))) :
            attempts -= 1
            print(f"Error , You Have Now {attempts} Try!") 
            ask = input("Are You New Here? (y/n): ")
            if ask in("y" , "Y"):
                print("❌The account does not exist. Please go to register‼️")
                return False
                
            else :
                print(f"Error , You Have Now {attempts} Try!") 
                print("❌You are write wrong User Name or password, Please Register First‼️")
                
        elif (users[userName]["Password"] == password) :
            print("Login Successfully✅") 
            print("Go To The Bank Menue...") 
            return True
    
    print("Your attempts ended and you are returned to main menue")
    return False

def checkBalance():
    print(f"Your Balance : {users[userName]["Balance"]} EGP.")
    
def deposit():
    dAmount = float(input("Plealse Enter Your Amount You Want To Deposit it: "))
    while dAmount <= 0 :
        print("Amount < 0 !!!")
        dAmount = float(input("Please Enter Amount > 0 : "))
    
    print(f"Your Balance Befor Deposit is {users[userName]["Balance"]}")
    users[userName]["Balance"]+= dAmount 
    users[userName]["lastTransaction"] = f"\nDeposit {dAmount} EGP💸\n"
    print("Deposit Successfull✅")
    # print(f"Your Balance Now is {users[userName]["Balance"]}")
    
    printReceipt("Deposit", dAmount)
    

def withdraw() :
    wAmount = float(input("Plealse Enter Your Amount You Want To Withdraw it: "))
    while wAmount <= 0 or wAmount > users[userName]["Balance"] :
        print("❌The amount is invalid or your balance is insufficient‼️")
        wAmount = float(input("Please Enter Sufficient Amount  : "))
    
    print(f"Your Balance Befor Withdraw is {users[userName]["Balance"]}")
    users[userName]["Balance"]-= wAmount 
    users[userName]["lastTransaction"] = f"\nWithdrew {wAmount} EGP💸\n"
    print("Withdraw Successfull✅")
    # print(f"Your Balance Now is {users[userName]["Balance"]}")
    
    printReceipt("Withdraw", wAmount)

def transfer() :
    global userName
    recipientName = input("Please Enter The Recipient's Name: ").strip().capitalize()
    
    while recipientName not in users :
        print("This user Dose not Exist!")
        ch = input("Are you want to register this account? (y/n): ")
        if ch in ("y" , "Y") :
            Register()
            break
        else :
            return
       
    if userName != recipientName :
        tAmount = float(input("Plealse Enter Your Amount You Want To Transfer it: "))
        if tAmount > 0 and (users[userName]["Balance"] >= tAmount):
            
            print("===============================================")
            print(f"BEFOR Transfer user: {userName} Has Balance  {users[userName]["Balance"]}")
            print(f"Now AFTER Transfer user: {userName} Has Balance {users[userName]["Balance"]}")
            # print("===============================================")
                        
            users[userName]["Balance"]-= tAmount 
            users[recipientName]["Balance"] += tAmount
            users[userName]["lastTransaction"] = f"\bTransfered {tAmount} EGP💸\n"
                                                                  
            print("----------------------------------------------")
            print(f"BEFOR Transfer user: {recipientName} Has Balance {users[recipientName]["Balance"]}")
            print(f"Now AFTER Transfer user: {recipientName} Has Balance {users[recipientName]["Balance"]}")
            print("===============================================")
            
    else :
        print("❌You cannot transfer to yourself‼️")
    printReceipt("Transfer", tAmount, recipient=recipientName)
    

def changePassword():
    password = (input("Please Enter Your old Password: "))
    if (users[userName]["Password"] == password) :
        newPassword = (input("Please Enter Your New Password: "))
        while len(newPassword) < 6  or newPassword == "" :
            print("Password invalid , Password Must be AtLeast 6!!")
            newPassword = (input("Enter Your Password Again:  "))
        users[userName]["Password"] =  newPassword 
        print("Password Changed Successfully✅")
        return 
    
def changeUsername():
    global userName 
    oldName = userName
    
    print(f"Your Current username is : {oldName}")
    newName = (input("Please Enter Your New Name: ")).strip().capitalize()
    while newName in users   :
        print("User Name Exists‼️")
        newName = input("Please Enter Another Name: ").strip().capitalize()
    users[newName] = users[oldName]
    del users[oldName]
    userName = newName
    print("UserName Changed Successfully✅")
    return
    
def logout():
    global userName 
    userName = ""
    
main()
