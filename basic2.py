#Write a program for simple interset
principle=100000
rate=10
time=1
interest=(principle*rate*time)/100
print(interest)

#WAP to accept centigrade to farhaniet
c=float(input("Enter Temperature in C:"))
f=(9/5)* c+ 32
print(f)
 
#WAP for swapping
#method 1
val1=23
val2=43
temp=val1
val1=val2
val2=temp
print(val1)
print(val2)

#method 2
a=100
b=200
a=a+b #(100+200=300)
b=a-b #(300-200=100) b=100
a=a-b #(300-100=200) a=200

#Wap to enter a height of user in feet and convert to inch and cm
h=float(input("Height:"))
inch=h*12
cm=inch*2.54
print(inch)
print(cm)

#Reverse the number
num=123
a=num%10 #3
num=num//10 #num=12
b=num%10 #b=2
c=num//10 #num=1
rev=a*100+b*10+c*1 #300+20+1=321
print(rev)


#reverse 7 digit no.
num = 1234567
for i in range(7):
    a = num % 10
    num = num // 10
    print(a, end="")

