# Simple password Guess

# take no. of tries 

tries = 5

validPass = input("Enter your valid password :").strip()

userPass = input("Enter your password :").strip()

while userPass != validPass and tries > 0  :
    tries-=1    
    if tries == 0 :
        print("All tries is finshed.")
        break
    userPass = input(f"Wrong password\nYou have now {"no" if tries == 0 else tries} tries\nPlease Enter your password agin :").strip()
print("loop is done ")
