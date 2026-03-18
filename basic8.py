# #print an integer representing the number of special characters and whitespaces present in the given message
# #method1
# msg = input("Enter your message: ")
# count = 0
# for char in msg:
#     if not char.isalnum():  
#         count += 1
# print(count)

# #method2
# import re
# var='nfsrrsd$%guyyuyu*'
# count=0
# for i in var:
#     #z = re.findall('[a-z,0-9]',i)
#     z=ord(i)
#     #print(z)
#     #if z:
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
#     print(count)

               
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)


# #Move Zeros to the End:
# #Q:Given an Array , move all the zeros to the end without changing the order of non- zero elements.
# def move_zeros(arr):
#     n = len(arr)
#     pos = 0  
#     for i in range(n):
#         if arr[i] != 0:
#             arr[pos] = arr[i]
#             pos += 1
#     while pos < n:
#         arr[pos] = 0
#         pos += 1
#     return arr
# arr = [0, 1, 9, 8, 0, 4, 0, 0, 2, 7]
# print(move_zeros(arr))


# #Move zeros to end o the list
# A=[0,1,0,3,12]
# for i in A:
#   if i==0:
#     A.remove(0) # or A.remove(i)
#     A.append(0) # or A.append(i)
# print(A)


# #Find the second largest element:
# # Q:Find the second largest element in an array
# arr = [12, 35, 1, 10, 34, 1]
# unique = list(set(arr))
# unique.sort(reverse=True)
# if len(unique) >= 2:
#     print("Second largest:", unique[1])
# else:
#     print("No second largest element")


# #Finding the total distance between adjacent terms of list of 5 numbers
# arr = [5, 10, 3, 12, 7] 
# total_distance=0 
# for i in range(len(arr) - 1):
#     total_distance += abs(arr[i+1] - arr[i])
# print("Total distance:", total_distance)


