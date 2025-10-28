#logical operators

print(45>5 and 45<10 ,"false")
print(45>5 or 45<100 ,"true")
print(not(45>5),"false")

#conditional statements in python
#if, elif, else

a = 0
#indentation
if a>0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")
print("hi")

age = -56
 
if age >= 18: 
    print("Eligible to vote") 
else: 
    print("Not eligible")


marks = 6
if marks >= 40 and marks <= 100: 
    print("Pass") 
else: 
 

    print("Fail") 

amount = 650
coupon =  "SAVE10"
 
if amount >= 500 and coupon == "SAVE10": 
    print("Discount Applied") 
else: 
    print("No Discount") 

x = 88
if x < 0 or x > 100: 
    print("Out of range") 
else: 
    print("Within range")

# 1. Input two numbers and check if they are equal. 
# a = int(input("enter a number"))
# b = int(input("enter a number"))

# if a==b:
#     print("equal")
# else:
#     print("not equal")

# 4. Accept three numbers and check which is the greatest.
a = 67
b = 78
c = 78

# if a>b and a>c:
#     print("a is the greatest")
# elif b>a and b>c:
#     print("b is the greatest")
# else:
#     print("c is the greatest")

# 5. Write a program to accept age and print whether the person is a child, adult, or senior 
# (use multiple conditions). 
a = 1

if a<5:
    print("child")
elif a>6 and a<14:
    print("young")
elif a>15 and a<60:
    print("adult")
else:
    print("senior")
