# using input () function
'''
variable = input()
variable = data-type(input(__))
by defalut input function takes string as input to chnage the input data type use typecasting function before input.
'''

a = input("Enter your name: ")
print("My name is ",a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x+y) #it will concatinate the input
print(int(x)+int(y))

#now the input is converted while taking input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(x+y)


