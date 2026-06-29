print("Welcom to you in my program")
python = input("Are you proficient in Python? (Yes/No) : ").strip().lower()

if python in ("yes" , "y"):
    exp = int(input("How many years of experience or projects ? "))
    certificate = input("Do you have a university degree in computer science OR bootcamp? (Yes/No) :").strip().lower()
    if (exp >= 2) and (certificate in ("yes" , "y")):
        print("Congratulations! You have been accepted to the next stage of interviews.")
    else :
        print("Sorry, your current qualifications do not match the job requirements.")  
        
else : 
    print("Sorry, your current qualifications do not match the job requirements.")  
