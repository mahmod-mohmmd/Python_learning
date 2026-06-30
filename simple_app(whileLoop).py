# Empty list to fill later
myfavouritWebs = []

# take num of max allowed webs
maxWebs = int(input("Enter num of webs: "))
 
while maxWebs > 0 :
    # input new web
    web = input("Enter your websites: ")
    
    # add the new web to the list
    myfavouritWebs.append(f"https://{web.strip().lower()}")
    
    #Decrese num of webs from maxallowed
    maxWebs -= 1 
    
    print(f"Website added and remain {maxWebs} now")
    print(myfavouritWebs)
print("Bookmark is full ,you cannot add more")

# check if list is not empty 
if len(myfavouritWebs) > 0 :
    print("list not empty its contains :")
    # sort the list 
    myfavouritWebs.sort()
    i = 0 
    while i < len(myfavouritWebs) :
        print(myfavouritWebs[i])
        i+= 1 