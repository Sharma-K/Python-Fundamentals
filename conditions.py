# Conditional statement
x = int(input("Enter the value of x"))
if x > 20 or x == 10:
    print("True")
else:
    print("False") 

x = 50

if x == 10:
    print("inside if")
elif x == 50:
    print("inside else if")
 

check = True if x != 50 else False
print(check)