# Variable Intialize
x = 10
s = "This is a string"


# Conditional statement
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

# input
input = input()
print(input)

# Loop
counter = 0
while counter < 4:
    print(counter)
    counter += 1


for x in range(4):
    print(x)


sample = "keshav"

print(sample*2)
print(sample[2:4])
print(sample[-1]+sample[1])