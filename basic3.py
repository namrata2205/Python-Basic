#mylist=["prashant","Ashish","riya",77,"ram","dev","om",60.23,"priya"]
#print(mylist)
#print(type(mylist))
#print(mylist[0])
#print(mylist[1])
#print(mylist[2])
#print(mylist[-1])
#print(mylist[2:5])
#print(mylist[:5])
#print(mylist[1:])
#print(mylist[1:8:2]) #print 1 to 8 and then will increment by 2
#print(mylist[:])
#print(mylist[::-1])

#mylist.append('harsh')
#mylist.append('laxman')
#print(mylist)

#mylist.insert(1,"Sum")
#print(mylist)

#mylist.remove("priya")
#print(mylist)

#newlist = mylist.copy() #cloning
#print(mylist)
#print(newlist)


#multidimensional list
#mylist=[['dev','ram'],['86.5'],[40040,'yyyy']]
#print(mylist)
#print(mylist[row][col])
#print(mylist[0][0])
#print(mylist[0][1])
#print(mylist[1][0])
#print(mylist[2][0])
#print(mylist[2][1])


#list1=['prashant','jha']
#print(list1*2)  #it will print 2 times
#list2=[50,25,50]
#print(list1+list2)

#list2=[50,50.2,'prashant']
#del list2[2]
#print(list2)
#del list2
#print(list2) #will give error as complete list is delete so will unable to print


#list2=[50,50.2,'prashant']
#list2.clear()
#print(list2)


#name='prashant'
#print(name)
#myname=list(name) #typecasting
#print(myname)



#Sorting example
#mylist=[44,22,77,0,9,88] #0,9,22,44,77,88
#mylist.sort()
#print(mylist) #1)default sorting order is ascending 2)default for string is alphabetical order 3)we should know that list should contain homogenous data otherwise typeerror
#desending
#mylist=[44,22,77,0,9,88]
#mylist.sort(reverse=True)
#print(mylist)


#to return address
#math=10
#print(id(math))

#math =50
#phy =50
#print(id(math))
#print(id(phy)) #python will not directly assign the address to the variable first it check whether value already exist Eg:math =50 phy =50

#math =50
#phy =540
#print(id(math))
#print(id(phy)) 


#mylist=[44,55,66]
#newlist=mylist
#print(id(mylist))
#print(id(newlist))


#CONDITION
#two special type of membership opartor=1)in 2)not in
#name='prashant'
#print('z'in name)
#print('z' not in name)


#LOOP
#for i in range(6):
#   print(i)

#for i in range (2,6): #starting index from 2
#    print(i)

#for i in range (2,6,2): #increment by 2
#   print(i)

#for i in range (5,0,-1): #decsending
#    print(i)

#for i in range (1,6):
#   print(i*2)

#for i in range(1,11):
#    for j in range(1,11):
#        print(i*j, end="\t")
#    print()

#Simple if
#WAP to accept any digit and check pos,neg,zero
#no=int(input("enter value:"))
#if no>0:
#    print('postive')
#if no<0:
#    print('negative')
#if no==0:
#    print('Zero')


#WAP to accept days and check the working days and weekend
#days=input('Day:')
#if days=='Sat'or 'Sun' or 'sat' or 'sun':
#    print("Weekend")
#else:
#    print("Working days")


#WAP to accept three paper marks and calculate total,percentage and if percentage is greater then equal to 60 then he/she is eligible foe placement
#p=int(input("Marks1:"))
#m=int(input("Mark2:"))
#v=int(input("Marks3:"))
#per=(m+p+v)/300*100
#print(per)
#if per >= 60:
#    print("Eligible")
#else:
#    print("not Eligible")


#WAP accept five different value in 5 different var and check max value and print by using "simple if"
n1=int(input('Num1:'))
n2=int(input('Num2:'))
n3=int(input('Num3:'))
n4=int(input('Num4:'))
n5=int(input("Num5:"))
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print(n1+"Largest")
if n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print(n2+"Largest")
if n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print(n3+"Largest")
if n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print(n4+"Largest")
if n5>n1 and n5>n2 and n5>n3 and n5>n4:
    print(n5+"Largest")


