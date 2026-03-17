# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1   #both will have same address
# fruit_list3 = fruit_list1[:] #different address as value is assigned 
# fruit_list2[0] = 'Guava'    #will update value as guava in both list1 & list2 as same address
# fruit_list3 [1] = 'Kiwi'    #will update value as kiwi in list3

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':  #list1[0]=Guava true  #list2[0]=Guava true  #list3[0]=Guava false
#         sum+=1            #sum=1                #sum=2                #sum=2
#     if ls[1]=='Kiwi':     #list1[1]=Kiwi false  #list2[1]=kiwi false  #list3[1]=kiwi true
#         sum+=20                                                       #sum=22
# print(sum)


# def f(i,values=[]): #default list
#     values.append(i)
#     print(values)
#     #return values
# f(1)
# f(2)
# f(3)


# def func(value,values): #value=3, value=[1,2,3]
#     var = 1
#     values[0]=44    #[44,2,3]
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])


# dict = {'c':97, 'a':96, 'b':98}
# for _ in sorted (dict):  #can use _ if we don't want to keep any variable #make sure to not write error as an o/p
#     print(dict[_])


# fruit = {}
# def addone(index):
#     if index in fruit : # list empty therefore Apple = false, list[1]=Banana=>false list[2]=apple=> false
#         fruit[index]+=1
#     else:
#         fruit[index]=1  #[Apple:1,Banana:1,apple:1] 
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))


