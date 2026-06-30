# print("i love python") 
# print("i love programing") # this is inline comment
#_______________________

    # COMMENTS 

#Information about file 
# who created the file 
#when the file created
#why the file is created
#write beside the programming line 
#write before the programming line 


"""
this is 
NOT 
multiple 
line 
comment
"""
#_______________________

    #DEAL WITH DATA
# type() ->  show datatype of data 
# all data in python is objects
#--------
# print(type(10))
# print(type(10.5)) # floating point number
# print(type("Hello python!"))

# print(type(2==2)) #this is boolean

# print(type([1,2,3,4,5])) # this is list
# print(type((1,2,3,4,5))) # this is Tuple
# print(type({"one":1 , "two":2 ,"three":3 })) # this is dictionary

#_______________________

    #VARIABLES p1
# myVar = "my value"
# print(myVar)

# name = "mahmoud" #single word => normal
# myName = "mahmoud" #two words => camelCase
# my_name = "mahmoud" #two words => snake_case

#_______________________

    #VARIABLES p2

# x = 10 
# x = "hello"
# print(x) 

# reserved words 
# help("keywords")
#------
# a, b, c = 1,2,3
# print(a)
# print(b)
# print(c)

#_______________________

    #Escape sequences characters
    
# # \b = back space
# print("hello\b world") # will remove o

# # \ = newLine
# # print("hello
# #       i love 
# #       python") # this is wrong
# print("hello \
# i love \
# python")

# #Escape back slash by \
# print("I love back slash \\") 

# #Escape  quote
# print("I love back slash 'test'") 
# # or by \' \'
# print('I love back slash \'test\'') 

# # \n line feed 
# print("hello world \nI love python ")

# #\r carriage return
# print("123456\rabcd")

# #\t horizontal tab
# print("Hello\tpython")

# # \xhh hexa value 
# print("\x4f\x73")

#_______________________

#     #Concatenation
    
# msg = "i love "
# lang = "python"
# print(msg + lang)

# a = "first \
# second \
# third "

# b = " F \
# S \
# T"

# print(a+"\n"+b)

# print("hello " + 1) # this is not valid 

#_______________________

    #Strings

# mystr1 = "this is double quote"
# mystr2 = "this is single quote"
# mystr3 = "this is single quote 'test' "

# print(mystr1)
# print(mystr2)
# print(mystr3)

# mystr5 ="""
# first "test"
# second 'test'
# third
# """
# mystr6 = '''sfirst 'test'
# ssecond "test"
# sthird'''

# print(mystr5)
# print(mystr6)

#_______________________

    #Strings (indexing & slicing)
    
# # indexing (access item)
# mystr = "i love python"
# print(mystr[9])

# #slicing (access multiple sequence items)
# #[start:end:steps]
# mystr = "i love python"
# print(mystr[:9])
# print(mystr[::2])

#_______________________

    #Strings Methods

    # 1. strip(), rstrip() , lstrip() => remove spaces 
# mystr = "   i love python    "
# print(mystr)
# print(mystr.strip())
# print(mystr.rstrip())
# print(mystr.lstrip())
# print(len(mystr))

# mystr = "*****i love python*****"
# print(mystr)
# print(mystr.strip("*"))
# print(mystr.rstrip("*"))
# print(mystr.lstrip("*"))

    #2. title() => 1st letter from word capital and letter after nums also

# b ="I love 2d and graphics and 3g technology and python"

# print(b.title())

    #3. capitalize() 1st letter from all words capital
# b ="i love 2d and graphics and 3g technology and python"

# print(b.capitalize())

    #zfill
# c ,d, e = "1" ,"11" ,"111"
# print(c.zfill(3))
# print(d.zfill(3))
# print(e.zfill(3))

    # split() rsplit()
# a = "I love python and php"
# print(a.split())

# b = "I-love-python-and-php"
# print(b.split())
# print(b.split("-"))

# c = "I-love-python-and-php"
# print(c.split("-" ,3))
# print(c.rsplit("-" ,3))

    #center()
# e = "Mahmoud"
# print(e.center(15)) # spaces
# print(e.center(15, "#")) # hashes

    # count()
# f = "I love python and php because php is easy"
# print(f.count("php"))

    # index()
# a = "I love python"
# print(a.index("p"))
# print(a.find("p",0,5)) # error

 # find()
# a = "I love python"
# print(a.find("p",0,5)) # -1

 # # splitlines()
# e = """first line
# second line
# third line"""
# print(e.splitlines()) 

#  # join() itarable
# mylist = ['mahmoud' , 'mohamd' , 'gomaa']
# print(' '.join(mylist))
# print(type(' '.join(mylist)))


    #String formatting (old ways)
    
# name = "mahmoud"
# age = 20 
# rank = 10 
# # print("my name is "+ name + " and my age is "+age+ " i have rank "+ rank) #type error

# print("my name is %s"% "Mahmoud")
# print("my name is %s and my age is: %d" % (name, age))
# print("my name is %s and my age is: %d and my rank is:%f" % (name, age ,rank))

# n = "Aborgeila"
# l = "Python"
# y = 20
# print("Iam %s i learn %s and i have %d years old" %(n ,l,y))

# # control floating point number

# my_num = 10
# print("my num is: %d " %my_num)
# print("my num is: %f " %my_num)
# print("my num is: %.2f " %my_num)

# # slice string (truncate)

# myLongString = "hello iam mahmoud i have 20 years old and iam from giza and i learn pyton now"
# print("message is %s" % myLongString)
# print("message is %.10s" % myLongString)

    #String formatting (new ways)

# name = "mahmoud"
# age = 20 
# rank = 10 
# # print("my name is "+ name + " and my age is "+age+ " i have rank "+ rank) #type error

# print("my name is {}".format("Mahmoud"))
# print("my name is {} and my age is: {}" .format(name, age))
# print("my name is {:s} and my age is:{:d} and my rank is:{:.3f}".format(name, age ,rank))

# n = "Aborgeila"
# l = "Python"
# y = 2
# print("Iam {} i learn {} and i have {} years Exp" .format(n ,l,y))

# control floating point number

# my_num = 10
# print("my num is:{} ".format(my_num))
# print("my num is: {:f} " .format(my_num))
# print("my num is:{:.2f} " .format(my_num))

# slice string (truncate)

# myLongString = "hello iam mahmoud i have 20 years old and iam from giza and i learn pyton now"
# print("message is {}" .format(myLongString))
# print("message is {:.17s}" .format(myLongString))

    #format money
# myMoney = 5001746819172102
# print("my money in bank is:{:d}" .format(myMoney))
# print("my money in bank is:{:_d}" .format(myMoney))
# print("my money in bank is:{:,d}" .format(myMoney))
# print("my money in bank is:{:&d}" .format(myMoney)) # wrong

#     #ReArreng Items
# a , b, c = "one" ,"two" , "three"
# print("hello {} {} {} " .format(a,b, c))
# print("hello {} {} {} " .format(b,a, c))
# print("hello {1} {0} {2} " .format(a,b, c))
# print("hello {2} {1} {0} " .format(a,b, c)) # revers

# x , y , z = 10 ,20 ,30 
# print("hello {} {} {} " .format(x, y ,z))
# print("hello {1} {0} {2} " .format(x, y ,z))
# print("hello {2:.2f} {1:.2f} {0:.2f} " .format(x,y,z)) # revers

    #format in version  3.6+ (best way)
# myName = "aborgeila"
# myAge = 20 
# print("My name is {myName} and my age is {myAge}")
# print(f"My name is {myName} and my age is {myAge}")

    # complex numbers
# print(type(5+6j))
# complexnumm = 5+6j
# print(f"Real part is {complexnumm.real}")
# print(f"Real part is {complexnumm.imag}")

#     #floor division
# print(100 // 20) #5
# print(100 // 20) #5
# print(120// 20 ) #6
# print(130// 20 ) #6

    # Lists 

# myList = [1, "one" ,1.5]
# print(myList)

# myList[1] = 2 
# print(myList)
# myList[0:2] = []
# print(myList)

# myList[0:2] = ["a" ,'b']
# print(myList)

    #Lists Methods
# append()
# myOldFrinds = ["A",'B','C','D']
# myFrinds = ['a' ,'b' ,'c' ,'d']
# print(myFrinds)
# myFrinds.append('e')
# print(myFrinds)

# myFrinds.append(myOldFrinds)
# print(myFrinds)
# print(myFrinds[5][2])

# # extend()
# a =[1,2,3,4]
# b =['a','b','c','d']
# a.extend(b)
# print(a)

# # remove()
# x =[1, 2, 3, 4, 'a', 'b', 'c', 'd']
# x.remove(2)
# print(x)

#     # sort()
# y = [1,4,7,6,2,8,5,0,3]
# print(y)
# y.sort()
# print(y)
# y.sort(reverse=True)
# print(y)

#     # reverse()
# # z = [10 , 1, 9 , 80 , 100 ,"mahmoud" ,100]
# # z.reverse()
# # print(z)

#     #clear()
# a = [1,2,3,4]
# a.clear()
# print(a)

#     #copy()
# b = [1,2,3,4]
# c = b.copy()
# print(b)
# print(c)
# b.append(5)
# print(b)
# print(c)

#     #count()
# b = [1,2,3,1,3,5,7,8,4,2,7,3,1,9,3,4,6,7,1,4]
# print(b.count(1))

#     #insert()
# f =[1, 2, 3, 4, 'a', 'b', 'c', 'd']
# f.insert(0, "test")
# print(f)

#     #pop()
# a = [1,2,3,4]
# print(a.pop(1))

    #Tuples 
# myTuple1 = ("aborgeila", "mahmoud" , "mohamed" )
# myTuple2 = "aborgeila", "mahmoud" , "mohamed"  # we can make tuple without ()
# print(type(myTuple1))
# print(type(myTuple2))

#  # tuples are orderd and indexed but immutable
# print(myTuple1[0])
# print(myTuple1[-1])

#  # tuple not assign new values
# myTuple3 = (1,2,3,4,5,6,7,8)
# myTuple3[3] = "three" # error

# myTuple1 = ("mahmoud",)
# myTuple2 = "mahmoud",
# print(type(myTuple1))
# print(type(myTuple2))

# a = (1,2,3,4)
# b = (5,6,7)
# c= a+b
# print(c)

#  # tuple , list , string repeat (*)
# mystr = "mahmoud"
# mylist = [1,2,3]
# mytuple = ("a","b")

# print(mystr * 3 )
# print(mylist * 3 )
# print(mytuple * 3 )

#  # tuple destruct 
# a = ("a","b", 3,"c")

# # x ,y , z  = a # error
# x ,y ,_, z  = a 

# print(x)
# print(y)
# print(z)

#     #SETS is not orderd and not indexed
# mySet1 =  {"mahmoud" ,"aborgeila" ,100}
# print(mySet1)
# # print(mySet1[0]) # error

#  # items in set must be unique
# mySet2 = {"a" ,"A" ,"b" ,"B","B"}
# print(mySet2)

# a = {1,2,3,4}
# print(a)
# a.clear()
# print(a)

# b = {"one", "tow" ,"three"}
# c = {"1", "2" ,"3"}
# print(c.union(b))
# c.add("4")
# print(c)

#  # update()
# j = {1,2,3,4}
# k = {1,"one" ,"two"}
# j.update(k)
# print(j)

 
#  # difference()
# a = {1,2,3,4}
# b = {1,2, "mahmoud", "mahmoud"}
# print(a)
# print(a.difference(b)) #a- b

#  # difference_update()
# a = {1,2,3,4}
# b = {1,2, "mahmoud", "mahmoud"}
# print(a)
# a.difference_update(b) #a- b
# print(a)

#  # symmetric_difference()
# i = {1,2,3,4,5,"x"}
# j = {'mahmoud' ,'aborgeila' ,1,2,3}
# print(i)
# print(i.symmetric_difference(j))
# print(i)

    #Dictionary
# user = {"Name" : "Mahmoud",
#         "Age" : 20 ,
#         "County" : "Egypt",
#         "Skills":["html","css", "js"],
#         "Rating": 10.5 ,
#         "Name" : "Aborgeila"   # key must be unique
#         }
# print(user)
# print(user["Name"])
# print(user.keys())
# print(user.values())

#  # Two dimensional dictionary
# lang = {
#     "one":{
#         "name" : "html",
#         "progress" : "60%"
#         } ,
#     "two":{
#             "name" : "css",
#             "progress" : "50%"
#         },
#     "three":{
#             "name" : "python",
#             "progress" : "80%"
#         }
# }

# print(lang)
# print(lang["one"])
# print(lang["three"]["name"])
# print(len(lang))
# print(len(lang["one"]))

 # create dict from variables
# framwork_one = {
#         "name" : "vuejs",
#         "progress" : "60%"
#     }
# framwork_two = {
#         "name" : "ReactJs",
#         "progress" : "80%"
#     }
# framwork_three= {
#         "name" : "angular",
#         "progress" : "70%"
#     }

# all_framworks ={
#     "One" : framwork_one ,
#     "Two" : framwork_two ,
#     "Three" : framwork_three 
# }

#  # Methods
# print(all_framworks)
#  # clear()
# all_framworks.clear() 
# print(all_framworks)

#  # update()
# member = {
#     "name" : "mahmoud"
# }
# print(member) 
# member["age"] = 20
# print(member) 
# member.update({"county": "egypt"})
# print(member) 

#  #copy()
# b = member.copy()
# print(b)
# member.update({"phone":"011"})
# print(member)
# print(b)

 
#  # popitem()
# member = {
#     "name" : "mahmoud",
#     "skill" : 'ps4'
# }
# print(member)
# print(member.popitem())

#  # items()
# all_items = member.items()
# print(member)
# member['age'] = 20 
# print(member)
# print(all_items)

#  # fromkeys()
# a = ("keyone","keytwo","keythree")
# b = "x"

# print(dict.fromkeys(a ,b))

#     # Boolean
# name = " "
# print(name.isspace())
# print(100 > 200)
# print(100 > 100)
# print(100 > 90)

#  # True values
# print(bool("Mahmoud"))
# print(bool(100))
# print(bool(54.66))
# print(bool(True))
# print(bool([54,66,'a']))

#  # False values
# print(bool(0))
# print(bool(False))
# print(bool(''))
# print(bool(""))
# print(bool([]))
# print(bool(None))
# print(bool(not True))

#     # boolean operators
#  # and
# age = 20 
# country = "egypt"
# print(age > 18 and country == "egypt")
#  # or 
# print(age > 18 or country == "KSA")
 # not
# print(age > 18)
# print(not age > 18)

    #type conversion
 # str()    
# a = 10
# print(type(a))
# print(type(str(a)))

#  #tuple() must to be iterable to convert to tuple
# c = "mahmoud" # str
# d = [1,2,3,4,5] # list
# e = {'a' , 'b' ,'c'} # set
# f = {"a" : 1 ,"b" : 2 ,"c" : 3 } # dict

# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))
# print(tuple(500)) #not iterable


#  #list() must to be itarable to convert to list
# c = "mahmoud" # str
# d = (1,2,3,4,5) # tuple
# e = {'a' , 'b' ,'c'} # set
# f = {"a" : 1 ,"b" : 2 ,"c" : 3 } # dict

# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))
# print(list(500)) #not iterable

#  #set() must to be itarable to convert to set
# c = "mahmoud" # str
# d = (1,2,3,4,5) # tuple
# e = ['a' , 'b' ,'c'] # list
# f = {"a" : 1 ,"b" : 2 ,"c" : 3 } # dict

# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))
# print(set(500)) #not iterable

 # dict() must to be nested to convert to dict
# c = "mahmoud" # string cannot be convert to dict error

# d = (1,2,3,4,5) #this tuple is not convert to dict
# D = (('a',1),('b',2),('c',3)) # nested tuple can convert to dict by key and value

# e = ['a' , 'b' ,'c'] # this list is not convert to dict
# E = [['a',1],['b',2],['c',3]]  # nested list can convert to dict by key and value

# f = {{"aa" , 11} ,{"bb",22}} # set cannot everyway

# print(dict(c)) 
# print(dict(d))
# print(dict(D))
# print(dict(e))
# print(dict(E))
# print(dict(f))
# print(dict(500)) #not iterable

#     # User input

# fName = input("What\'s Your first name ? ")
# mName = input("What\'s Your middel name ? ")
# lName = input("What\'s Your last name ? ")

# fName = fName.strip().capitalize()

# mName = mName.strip().capitalize()

# lName = lName.strip().capitalize()

# print(f"Hello {fName} {mName:.1s} {lName}")

#     # slice Email
    
# email = "aborgeila@gmail.com"
# # print(email[0:9])
# print(email[:email.index("@")])
# domain = (email[email.index('@')+1:email.index('.')])
# print(domain)

    # practical your age full details
    
# age = int(input("What'\s your age ? ").strip())
# print(age)
# print(type(age))

#  # get age in all time units
# months = age * 12
# weeks = months *4 
# days = age * 365
# hours = days *24 
# minutes = hours * 60 
# seconds = minutes *60 

# print ("You Libed For")
# print(f"{months} Months.")
# print(f"{weeks} Weeks.")
# print(f"{days:,} Days.")
# print(f"{hours:,} Hours.")
# print(f"{minutes:,} Minutes.")
# print(f"{seconds:,} Seconds.")


#     # if - else - elif 
# uName = "aborgeila"
# uCountry = "Egypt"
# isStudent  = "Yes"
# cName = " python course"
# cPrice = 250
# cDiscount = 30
# if uCountry == "Egypt" :
#     if isStudent == "Yes" :
#         cDiscount = 90 
#         print(f"Hello {uName} because you are from {uCountry} and student")
#         print(f"the course \"{cName}\" price is : ${cPrice-cDiscount}")
        
# elif uCountry == "KSA" :
#     cDiscount = 50
#     print(f"Hello {uName} because you are from {uCountry}")
#     print(f"the course \"{cName}\" price is : ${cPrice-cDiscount}")
    
# else :
#     print(f"Hello {uName} because you are from {uCountry}")
#     print(f"the course \"{cName}\" price is : ${cPrice-cDiscount}")

#     # 

# country = "Egypt"
# if country == "Egypt":
#     print(f"the weaher in {country} Is 15")
# elif country == "KSA" :
#     print(f"the weaher in {country} Is 30")
# else : 
#     print("country not in the list")
    
    
# # short if

# moviRate = 18
# age = 20

# if age < moviRate : print("Movie s Not good 4u")
# else : print("Movie s good and happy watching")

# print("Movie s not good 4u" if age < moviRate else "Movie s good and happy watching" )
    
#     # 
# # collect age
# age = int(input("enter your age:"))

# # collect time 
# unit = str(input("choose time unit (months , weeks , days):").strip().lower())
# print(unit)

# #get time units
# months = age * 12
# weeks = months *4 
# days = age * 365

# if unit == "months" or "m" :
#     print("you choose the unit months")
#     print(f"you lived for {months:,} months")
    
# elif unit == "weeks" or "w" :
#     print("you choose the unit weeks")
#     print(f"you lived for {weeks:,} weeks")
# elif  unit == "days" or "d" : 
#     print("you choose the unit days")
#     print(f"you lived for {days:,} days")
# else :
#     print("your choice is wrong")

#     #
# counties1 = ["Egypt" , "KSA","Kuwait" , "Bahrain"]
# counties1discount= 80
# counties2 = ["Italy" , "USA"]
# counties2discount= 50
# mycountry = "USA"
# if mycountry in counties1 :
#     print(f"hello u have a discount ${counties1discount}")
# elif mycountry in counties2 :
#     print(f"hello u have a discount ${counties2discount}")
    
# else :
#     print("you dont have discount")

#     # loop (while)
# a = 0
# while a < 10 :
#     print(a)
#     a+=1 
# print('loop is done')

# while False :
#     print("will not print")

# myf = ['a','b','c','d','e','f','g','h','i','j']
# print(len(myf))
# a = 0 
# while a< len(myf):
#     print(f"{str(a+1).zfill(2)} = {myf[a]}")
#     a+=1 
# print("all f printed ")
 









