#Why python is called as dynamically typed language
math=40
pi=3.14
name='Namrata Thorat'
print (type(pi))
print (type(math))
print (type(name))


#What is type casting
print()
print(2+2)
print('2'+'2')
val1=int(input("Enter first value:")) #user input by default take string values
val2=int(input("Enter Second value:"))
print(val1+val2)


#Array is a collection of finite values

#which value is being typecasted
print()
print(int(3.14))
print(int(True))
print(int(False))
print(int('4'))
print(int(10+5j))
print(int("4.22")) #will not cast beacuse both float and string cannot be casted

print()
print(float(3))
print(float(True))
print(float(False))
print(float('4'))
print(float(10+5j))
print(float(4.22))


print()
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex('4'))
print(complex('5.6'))
print(complex(5,-3))
print(complex("name"))
print(complex(True,False)


#bool if we provide 0 in any format then we will get false
print()
print(bool(0))
print(bool(12))
print(bool(3.14))
print(bool(True))
print(bool(False))
print(bool())
print(bool(-1))
print(complex(0.0))
print(complex("name"))
