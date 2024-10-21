b = 1
print(type(b))


b = 1.9
print(type(b))


b = "this is test"
print(type(b))

# complex data type 
a = 2-3j
print(type(a))

# string
# same datatype + same datatype 

print("a "*10)

a = "hello"
b = "Kathmandu"
d = 10 
e = 11
c = "hello Kathmandu i am sudan 21"

print(a,b,"i am sudan")
print(a+" "+b)

# string formating or f string
print(f'{a} {b} i am sudan {d+e}')


# a = "11"
# b = "77"

# print(int(a)+int(b))

# c = 111
# print(type(c))

# d = str(c)

# print(type(d))

if (1==2):
    print ("this if if condition")
    a = 10
    print (a)
else:
    print ("this is else condition")
GPA = 3.25
if (GPA>=3.25 and GPA<=4.0):
    print ("this is distinction")
elif (GPA>=3.25 and GPA<=4.0):
    print ("this is pass")
else:
    print ("this is fail")


#     '''
# if(condition):
#     if(condition):
#         print("nested")
#     else:
#         print("nested else")
# else:
#     print("this is else")

# '''


if (1==1):
    print("this is true")
    if(1==4):
        if (2>=2):
            print("this is true for nested nested ")
        else:
            print("this is nested nested else")
        print("nested if ")
    else:
        print("nested else condtion")
else:
    print("this is false")

# #if (a==5):
#     print ("this is false")
#     if (a==6):
#         print ("this is true for nested nested")
#         else:
#             print ("this is nested nested else")
#     else:
#         print ("this is nested nested else")
# else:
#     print ("this is true")

#single line "if" condition
# #gender = female 
# result = "gender is female" if "gender is male" else "gender is male"
# print (result)