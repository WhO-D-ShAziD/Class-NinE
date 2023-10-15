# Project: 05 [Calculator Using Match Case]

a = int(input("Enter the first number:\n"))

b = int(input("Enter the second number:\n"))

op = input("Which kind of operation you want:\n")

match op:
    case "+":
        c = a + b
        print("The addition of the two numbers are: ", c)
    case "-":
        d = a - b
        print("The subtraction of the two numbers are: ", d)
    case "*":
        e = a * b
        print("The multiplication of the two numbers are: ", e)
    case "/":
        f = a / b
        print("The division of the two numbers are: ", f)
    case _:
        print("Invalid Operator!")


# echo "# Class-NinE" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/WhO-D-ShAziD/Class-NinE.git
# git push -u origin main