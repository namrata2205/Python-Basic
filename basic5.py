# # print output  
# # 1   5
# # 2   4
# # 4   2
# # 5   1
# for i ,j in zip(range(1,6),range(5,0,-1)): 
#     if i==3 and j==3:    
#         continue
#     print(i," ",j)


# i=1
# while i<=5:
#     print(i)
#     i=i+1


# username=''
# password=''
# while username!="admin" and password!="hello":
#     username=input("Enter username:")
#     password=input("Enter password:")


# n=int(input("Enter number:"))
# sum=0
# i=1 #initialization point i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("The sum of first",n,"numbers is:",sum)


# name='prashant' #o/p=prashnt
# newname=' '
# for i in name:
#     if i not in newname:
#         newname+=i
# print(name)
# print(newname)


# #write a program to reverse a string using any loop
# n='Namrata'
# rev=''
# for i in n:
#     rev=i+rev
# print(rev)
    
        
# mycart=[10,20,200,300,800,60,700] 
# for i in mycart:
#     if i>400:
#         print("This my purchased cart item")
#         continue
#     print(i)


# #palindrome
# s=input("Enter String:")
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("not Palindrome")


# #Anagrams
# s=input("Enter String1:")
# s2=input("Enter String2:")
# sorted(s)
# sorted(s2)
# if s in s2:
#     print("Anagrams")
# else:
#     print("Not anagrams")


# #Add key value pairs to a dictionary
# my_dict = {}
# my_dict["name"] = "Namrata"
# my_dict["age"] = 20
# print(my_dict)


# #Remove key value pairs from dictionary
# my_dict = {"name": "Namrata", "age": 20, "city": "Solapur"}
# del my_dict["age"]
# print(my_dict)


# #nested for loop
# for i in range(1,4): #outer loop => row's
#     for j in range (1,4): #inner loop => col's
#         print(i,end=' ')
#     print()


# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range (i,n+1):
#         print(chr(64+i),end =' ')#ASCII
#     print()


# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=' ')
#     print()