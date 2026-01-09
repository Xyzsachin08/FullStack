#list is mutable
# string is immutable
#tuple is immutable
#dictionary is mutable
#set is mutable


# immutable
'''x = 5
y = 10

print(id(x), id(y))

y+=1
print(id(x), id(y))



#mutable
list1 = ["sachin","nandini","shounak"]
list2 = ["bhushan","kiran","bhat"]


print(id(list1),id(list2))
list1.append("borude")
print(id(list1),id (list2))


#shalo & deep copy
import copy
a = [[1,2],[3,4]]
b = copy.copy(a)   #shalo copy
print(a,b)


c=copy.deepcopy(b)
print(c)'''




#genrat_the_random_password
import random
import string

n = int(input("Enter the legth of password:"))

characters = string.ascii_letters + string.digits
password = ""

for i in range(n):
    password += random.choice(characters)

print("Generated Password:", password)





