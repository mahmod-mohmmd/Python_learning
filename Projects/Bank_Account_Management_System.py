def main():
    while True :
            print("1. Enter To Program")
            print("2. Exit")
            choice = input("Choice (1/2): ")
            if choice == "1":
                mainManue()
            elif choice == "2":
                print("GoodBye!")
                break
            else:
                print("Invalid choice, try again.")
                
def mainManue():
        while True:
            print("\n=============================================")
            print("========== Welcom To Python Bank ============")
            print("=============================================")
            print(" Chose one of this choice : ")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choice (1/2/3): ")
            if choice == "1" :
                Register()

            elif choice == "2":
                if Login() == True:
                    bankMenue()
                
            elif choice == "3" :
                print("You Chose Exit.")
                break
            else :
                print("Invalid choice, try again.")
                
def bankMenue():
    while True :
        print("================================")
        print("========== Bank Menue ==========")
        print("================================")
        print(" Chose one of this choice : ")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Change Password")
        print("6. Logout")
        print("7. Main Menue")
        
        choice = input("Choice (1/2/3/4/5/6/7): ")
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
            logout() 
            break
        elif choice == '7': 
            mainManue() 
        else :
            print("Invalid choice, try again.")
            
users = {}
userName = ""

def Register():
    global userName
    print("You In Register.")
        
    userName = input("Please Enter Your Name: ").strip().capitalize()
    
    while userName in users   :
        print("User Name Exists!")
        userName = input("Please Enter Another Name: ").strip().capitalize()
    
    password = (input("Please Enter Your Password: "))
    
    while len(password) < 6  or password == "" :
        print("Password invalid , Password Must be AtLeast 6!!")
        password = (input("Enter Your Password Again:  "))
        
    users[userName] = {}
    users[userName] = {"Password" : password , "Balance" : 0}
    
    print("Registration Successful!")
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
                print("The account does not exist. Please go to register.")
                return False
                
            else :
                print(f"Error , You Have Now {attempts} Try!") 
                print("You are write wrong User Name or password, Please Register First.")
                
        elif (users[userName]["Password"] == password) :
            print("Login Successfull!") 
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
    print("Deposit Successfull!")
    print(f"Your Balance Now is {users[userName]["Balance"]}")
        

def withdraw() :
    wAmount = float(input("Plealse Enter Your Amount You Want To Withdraw it: "))
    while wAmount <= 0 or wAmount > users[userName]["Balance"] :
        print("AThe amount is invalid or your balance is insufficient.")
        wAmount = float(input("Please Enter Sufficient Amount  : "))
    
    print(f"Your Balance Befor Withdraw is {users[userName]["Balance"]}")
    users[userName]["Balance"]-= wAmount 
    print("Withdraw Successfull!")
    print(f"Your Balance Now is {users[userName]["Balance"]}")

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
            
            print("==========================================================================")
            print(f"BEFOR Transfer user: {userName} Has Balance  {users[userName]["Balance"]}")
            print(f"BEFOR Transfer user: {recipientName} Has Balance {users[recipientName]["Balance"]}")
            print("==========================================================================")
                        
            users[userName]["Balance"]-= tAmount 
            users[recipientName]["Balance"] += tAmount
            
            print("==========================================================================")
            print(f"Now AFTER Transfer user: {userName} Has Balance {users[userName]["Balance"]}")
            print(f"Now AFTER Transfer user: {recipientName} Has Balance {users[recipientName]["Balance"]}")
            print("==========================================================================")
            
    else :
        print("You cannot transfer to yourself")

def changePassword():
    password = (input("Please Enter Your old Password: "))
    if (users[userName]["Password"] == password) :
        newPassword = (input("Please Enter Your New Password: "))
        while len(newPassword) < 6  or newPassword == "" :
            print("Password invalid , Password Must be AtLeast 6!!")
            newPassword = (input("Enter Your Password Again:  "))
        users[userName]["Password"] =  newPassword 
        print("Password Change Successfull!")
        # print("Go to login page To sure for New Password...\n")
        return    
def logout():
    global userName 
    userName = ""
main()
