# variables are like empty containers in which data can be stored
# type of data stored in the variables are defined by data types
'''
1. NUMERIC
2. TEXT / STRING
3. BOOLEAN
4. LIST/TUPLE - combination of data of same data types[tuples] or different data types[list ]
5. DICTIONARY - collection of key-value pairs , map data {key : value}
'''

#HOW TO FIND THE TYPE(DATA TYPE) OF VARIABLE -- by using type(___) function

a = 1  # ineteger
b = True # boolean
c = "purvaaakshi" # string
d = None # null
list = [8,1.2,[-4,5],["apple",'banana']]
tuple = ["apple","banaan","strawberry"]
dic ={"name":"purvakshi","age":21}
print(a)
print(b)
print(c)
print(d)
print(list)
print(tuple)
print(dic)

print("The type of a is", type(a))
print("The type of b is", type(b))
print("The type of c is", type(c))
print("The type of d is", type(d))
print("The type of list is", type(list))