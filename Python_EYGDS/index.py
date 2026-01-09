
#input from user
'''name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
sub_result = num1 - num2
print(f"The sum of {num1} and {num2} is {sum_result}.")'''


#aggregate function
'''a = 10
b = 6


k=a**b
c=a+b 
d=a-b
e=a/b
t=a*b
s=a%b
print(c,d,e,t,s,k)'''

#grater than larger than

'''num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive:")
elif num <0:
    print("Tha number is negative:")
else:
    print("number is wrong")'''
    
    
    
# basic for loop
'''for i in range(1,8,2):
    print(i)
    
    
    
    
# 15 table 
v =1 
for i in range (15,151,15):
    print("15 *",v,"=",i)
    v+1
    
    
    
    
#plaindrome number    

s = int(input("enter a number:"))
temp = s
rev = 0

while s != 0:
    digit = s % 1
    rev = rev * 10 + digit
    s = s // 10

if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
    

print(121 == int(str(121)[::-1]))



#amsstrong  number


num = int(input("Enter a number: "))
temp = num
sum = 0

while num != 0:
    d = num % 10
    sum = sum + d*d*d
    num = num // 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''
    
    
    
    

#how to define  function in python 
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

print("This is a  sample python module with add and sunbtarct function ")

x = int(input("enter a number :"))
y = int(input("enter a second number :"))


print("addition",addition(x,y))
print("subtraction",subtraction(x,y))



