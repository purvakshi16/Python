# changing one data type into another is known as TYPECASTING
'''
two types of typecasting
1. Explicit - conversion of data type into another data type done via developer
            - it can be done by using pythons in-built type conversions functions
2.Implicit - according to the level of the data type one data type is converted into another automatically
            - python converts smaller data type to higher data type to prevent data loss
'''
a = "1"
b = "2" # value is written under quotes so they are considered as string
print(a+b) # 12
c = 1
d = 2 # now they are integers
print(c+d) # 3

# Explicit
print(int(a)+int(b))

# Implicit
e = 2.6
f = 2
# f will be converted from int to float
print(e+f)  #4.6
