print("Welcom to you in my program")
Price = int(input("Please enter price:"))
discount  = 0 
if Price < 100 :
    print("Sorry, No discount for you !")
elif 100 <= Price < 500 :
    discount = (10/ 100)*Price 
    print("You have discount 10%")
    print(f"Your price now is {Price - discount}")
else :
    discount = (20/ 100)*Price
    print("You have discount 20%")
    print(f"Your price now is {Price - discount}")
