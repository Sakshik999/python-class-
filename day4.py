# data type 
a = 4.3 # decimial value is known as float
a = 1 # integer 
a = "hello" #single or double cot is string 
print ("1" + "1")
print ("1" * 3)
print (3+3j) #complex / imaginary number 
a = 10
print ("type check", type (a))
b = "hello" 
print ("type check", type (b))
a = "11"
b = "200"
print (a+b)

# manual type cating 
a = 1 
print ("type check", type (a))
c = 2+3j
print ("type check", type (c))
x = '1'
print ('1' + '1')
a = "11"
b = "200"
print ("after type casting", int(a)+int(b))


test = "hello"
test2 = "from boardway"
test3 = 2222
# hello from boardway 2222
print ("type check", type (test), type (test2), type (test3))
print (test, test2, test3)

#string formatting 
print (f'{test} {test2} {test3}')
if (1==2):
  day = "Sunday"
  
day = "Sunday"
if (day=="Sunday"):
print ("Sunny day")