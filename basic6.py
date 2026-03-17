# #function
# def msg(): #called function
#     print("hello world")   
# msg()


# def add(): #called function
#     n1=int(input("Enter the value of n1:"))
#     n2=int(input("Enter the value of n2:"))
#     sum=n1+n2
#     mul=n1*n2
#     sub=n1-n2
#     div=n1/n2
#     return sum, sub, mul, div
# return = add()
# print(result)


#types of arguments 
#positional argument, keyword argument, default argument, variable length or variable number arguments
# #1] positional 
# def personalInfo(fname,lname):
#     print("first name=",fname)
#     print("Last name=",lname)
# personalInfo("Prashant",'jha')

# #2] KEYWORD
# def personalInfo(fname,lname):
#     print("first name=",fname)
#     print("Last name=",lname)
# fname='Prashant'
# lname='jha'
# personalInfo(fname,lname)

# #3] DEFAULT 
# def cityName(city='Nagpur'):
#     print(city)
# cityName("NAGPUR")
# cityName('delhi')
# cityName()

# #variable length argument
# def studentNames(*name):
#     print(name)
# studentNames("Prashant",'Rahul','Sandip',"Ashish")

# mylist=[5,2,9,7,5,6]
# #search the elements 7
# def searchElement(target):
#     for i in range (len(mylist)):
#         if target==mylist[i]:
#             print("Element found at index number",i)
# searchElement(7) #this element we have tto search

# mylist=[5,2,9,7,5,6]
# #search the elements 7
# def searchElement(target):
#     for i in range (len(mylist)):
#         if target==mylist[i]:
#             return i
#     return -1
# result=searchElement(10)    #7 this element we have to search
# if result!=-1:
#     print("elements found st index number=",result)
# else:
#     print("element not found")
