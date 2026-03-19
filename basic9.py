# #WAP to perform arithmatic operation using functional programming apporoach
# #Function helps us to acheive modularity approach
# import sys #in order to control infinite loop
# def addition(num1,num2): #called function
#     print("Addition:",num1+num2)

# # def substraction(): #called function
# #     pass                #pass keyword is used because we cannot keep the block empty

# def substraction(num1,num2): #called function
#     print("Substraction:",num1-num2)               

# def multiplication(num1,num2):   #called function
#     print("Multiplication:",num1*num2)

# def division(num1,num2): #called function
#     print("Division:",num1/num2)

# while True:
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     choice = int(input("Enter your choice from above options:"))
#     if choice == 5:
#         sys.exit()
#     val1 = int(input("Enter first Value:"))
#     val2 = int(input("Enter Second Value:"))
#     if choice == 1:
#         addition(val1, val2)
#     elif choice ==2:
#         substraction(val1,val2)
#     elif choice == 3:
#         multiplication(val1,val2)
#     elif choice == 4:
#         division(val1,val2)
#     else:
#         print("You have entered wrong value")


# #---------------------------------------------------------
# #nested function
# def outerFunction():
#     print("This is my outer function:") #second exe
#     def innerFunction():
#         print("Inner function") #third exe
#     innerFunction()
# outerFunction() # first exe start from here


# #----------------------------------------------------------
# #input = prashant is good programmer
# #WAP to count the word
# #output = 4
# name ="prashant is good programmer"
# count = 1
# for i in name:
#     if i == " ":
#         count += 1
#     else:
#         continue
# print("total word count ",count)


# #--------------------------------------
# init_tuple = {}
# print(init_tuple.__len__())


# #-------------------------------------------
# init_tuple_a = 'a','b'  #() is not mandatory in tuple
# init_tuple_b = ('a','b')
# print(init_tuple_a == init_tuple_b)


# #---------------------------------------------
# init_tuple_a = '1','2'
# init_tuple_b = ('3','4')
# print(init_tuple_a == init_tuple_b)


# #---------------------------------------------
# l = [1,2,3]
# init_tuple = ("Python",)*(l.__len__() -l[::-1][0])
# print(init_tuple)


# #-------------------------------------
# init_tuple = ('Python')*3
# print(type(init_tuple))


# #-------------------------------------
# init_tuple = (1,) * 3 
# init_tuple[0] = 2
# print(init_tuple) #error because value of tuple cannot change(immuteble)
 
 
# #-------------------------------------
# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8])) #The code outputs 4 because slicing init_tuple from index 3 to 8 captures the 4


# #---------------------------------------------
# # Replacing a string with another string:
# # s.replace (oldstring,newstring)
# # inside s, every occurrence of oldstring will be replaced with newstring
# s=""
# s1=s.replace("difficult","easy")
# print(s1)
# # All occurrences will be replaced
# s="ababababababab"
# s1=s.replace("a","b")
# print(s1)


# #-----------------------------------------------------
# # Removing spaces from the string
# # 1.rstrip()===>To remove spaces at right hand side
# # 2.lstrip()===>To remove spaces at left hand side
# # 3.strip()===>To remove spaces both side
# city=input("Enter your city name:")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderbadi..Abab")
# elif scity=='Chennai':
#     print("Hello Madrasi...Vanakkam")
# elif scity=='Bangalore':
#     print("Hello kannadiga... Shubhodaya")
# else:
#     print("your entered city is invalid")

    
    
    
# #------------------------------------------
# #list comprehension
# s=[i*i for i in range(1,11)]#i=5
# print(s)


# #-------------------------------------------
# val=[2**i for i in range (1,6)] #i=1,2,3,4,5
# print(val)


# #------------------------------------------
# s=[i*i for i in range(1,11)]#i=5
# print(s)
# val2=[i for i in s if i%2==0]
# print(val2)


# #------------------------------------------
# #Dictionary Comprehension:
# squares={x:x*x for x in range (1,6)}
# print(squares)

# #-----------------------------------------
# doubles={x:2*x for x in range (1,6)}
# print(doubles)