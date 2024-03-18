students = [
    ("Keshav", 12),
    ("Shiva", 23),
    ("Hemp", 54)
]

# Just like in C, printf("%d", i) we use "".format(...params)


# If you want leave empty curly braces it will automatically fill the params from left to right
for name, roll in students:
    print("Name:  {} and rollno: {}".format(name,roll))

# But if you want to print in certain order like I want to print roll first then name
    
for name, roll in students:
    print("Roll: {1} and Name: {0}".format(name, roll))


# Operations:
    
print(students + [('Addition',54)])
print(students*2)
