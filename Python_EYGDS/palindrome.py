# Palindrome Number

num = 121
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
