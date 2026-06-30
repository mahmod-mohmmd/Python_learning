# List contains admins
admins = ["Ahmed","Osama","Aborgeila","Mahmoud","Nada","3etra","Abdullah"]

# Login
name = input("Please Enter Your Name: ").strip().lower().capitalize()
#check name in admins
if name in admins :
    print(f"Hello {name.lower().capitalize()} welcom back ")
    option = input("Are you want to delete or update your name? (Y / N) ").strip().lower()
    if option == "y" :
        chosOption = input("Please Choose option:\n(1) Update \n(2) Delete \n").strip().lower()
        # update option
        if chosOption == "1" :
            old_name = input("Enter the name you want to update: ").strip().lower().capitalize() 
            new_name = input("Enter the new name: ").strip().lower().capitalize()
            admins[admins.index(name)] =  new_name 
            print("Name updated.")
            print(admins)
            
        # delete option
        elif chosOption == "2" :
            old_name = input("Enter the name you want to delete: ").strip().capitalize()
            admins.remove(old_name)
            print("Name deleted.")
            print(admins)
            
        else :
            print("worng option!")
            
else :
    print('You are not admin')
    opt = input("Are you want to added in the admins list? (Y / N) ").strip().lower()
    if opt == "y" :
        print("You have been added.")
        admins.append(name)
        print(admins)
    else : 
        print("You are not added!")
    
