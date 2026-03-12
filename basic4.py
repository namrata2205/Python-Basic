# #1)WAP to accept three paper marks and check maximum marks and check maximum marks using nested if else
# n=int(input("enter value1:"))
# m=int(input("Enter Value2:"))
# v=int(input("Enter Value3:"))
# if n>m:
#     if n>v:
#         print("n is greater");
#     else:
#         print("v is greater");
# else:
#     if m>v:
#         print("m is greater");
#     else:
#         print("v is greater");


# #2)WAP to accept percentage and if per
# #per>90==>'A'
# #per>80==>'B'
# #per>60==>'C'
# #per<60==>FAIL
# n=int(input("enter value1:"))
# m=int(input("Enter Value2:"))
# v=int(input("Enter Value3:"))
# per=(n+m+v)/300*100
# print(per)
# if per>=90:
#     print("A")
# elif per>=80 and per<90:
#     print('B')
# elif per>=60 and per<80:
#     print('C')
# else:
#     print("FAIL")
    
    
# #3)dictionary Datatype-> duplicate keys not allowed.  duplicate value allowed.
# mydict={
#     'name':'Namrata',
#     'professional':'Developer',
#     'empid':1002
# }
# print(mydict)
# print(type(mydict))


# #4)
# mydict={
#     101:'namrata',
#     102:'Riya',
#     '103':'Shweta',
#     '104':'Neha',
#     101:"Riya", #Overwrite 101:namrata thus 101:"Riya"
#     104:'Riya'
# }
# print(mydict)

# #5)write the help of key we have to print values
# a=mydict[102]
# print(mydict)

# #6)We will replace old value by new one
# a=mydict[102]='Shreya'
# print(mydict)

# #7)only print key x=0,1
# for x in mydict:
#     print(x)

# #8)only print values
# for x in mydict.values():
#     print(x)

# #9)Printing key and values both
# for x,y in mydict.items():
#     print(x,y)

# #10)if I have to add new key and value pair in my dictionary
# mydict['mobile_no']=4646478
# print(mydict)

# #11)imp:if we want to represent binary data like images,video
# mydict={
#     101:'namrata',
#     'professional':'developer',
#     'empid':101
# }
# mydict.pop("empid")
# print(mydict)


# #12)String Slicing
# name='prashantjha'
# #indexing =01234567910
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1]) #a
# #print(name[15])Error string index out of range
# print(name[0:5]) #end-1, 5-1=4 prash
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])


# #13)
# s='help4code is best platform for practicing programming'
# print(s.find('help4code'))
# print(s.find('python'))
# print(s.find('programming'))


# #14)
# s='namrata','ashish','sandip'
# m='|'.join(s)
# print(m)


# #15)
# s='Python is a high level programming language'
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


# # 16)
# print('Subjects marks:')
# p=50
# c=60
# m=70
# print('Pysics ={} chem ={} math={}'.format(p,c,m))
# print('Pysics ={0} chem ={1} math={2}'.format(p,c,m))
# print('Pysics ={x} chem ={y} math={z}'.format(x=p,y=c,z=m))
# total=p+c+m
# print("Total Marks",f"{total}")
# print("Roll No","7".zfill(4))


# #17)
# print('prashantjha777'.isalnum())  #True
# print('prashantjha'.isalpha())  #True
# print('777f'.isdigit())
# print('sdsdsd'.islower())
# print(''.islower())
# print("PRASHANTj".isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("hello".startswith("He"))
# print("Hello".endswith('lo'))


# #18)BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)  #160
# print((a-b)*(c/d))  #40
# print(a+(b*c)/d) #110


# #19)
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)


# #20)
# name='prashant'
# for i in name:
#     print(i) 


#21)
# name='prashant'
# data=['a','e','i','o','u']
# vowels=0
# con=0
# for i in name:
#     if i in data:
#          vowels+=1
#     else:
#         con+=1
# print(vowels)
# print(con)