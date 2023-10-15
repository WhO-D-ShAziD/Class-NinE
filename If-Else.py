# Mini Project: 04 

# Driving Lisence Eligibility



# name = input("Enter your name:\n")

# age = int(input("Please enter how old you are:\n"))

# money = int(input("How much money you can pay:\n"))

# if age>=18:
#     if  money>=5000:
#       print("You are eligible for the lisence!")
#     else:
#       print("You are not eligible")
# else:
#    print("Invalid Data!") 

name = input("Enter your name:\n")

age = int(input("Please enter your age\n"))

if age>=18:
    money = int(input("Please enter how much money you have:\n"))
    if money>= 5000:
        print("You are eligible for the lisence. Please contact later for the details!\n")
    else:
        print("You do not have enough money for the lisence!\n")
else:
    print("Your age is not eligible to have a driving lisence!\n")

print("Thanks for the interruption!\n")


