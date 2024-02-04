# DANYAL ABBAS
# N/A
# gamingindustry9@gmail.com

import sys

"""PYTHON CALCULATOR OR SMT

The program should follow these requirements:
• The calculator should continuously prompt the user for input until they choose to exit.
• The user should be able to select an operation by entering the corresponding number.
• After performing the calculation, display the result to the user.
• Handle invalid inputs gracefully and provide appropriate feedback to the user.
• Include an option for the user to exit the calculator. """


while True:
    print("Select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("Enter your choice (1, 2, 3, 4, 5): "))
    if choice == 5:
        print("Exiting the calculator. GoodBye!")
        sys.exit()
    elif choice > 5:
        print("input number out of range")
        continue

    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

    if choice == 1:
        print(f"Result : {num1} + {num2} = {num1+num2}")
    elif choice == 2:
        print(f"Result : {num1} - {num2} = {num1-num2}")
    elif choice == 3:
        print(f"Result : {num1} x {num2} = {num1*num2}")
    elif choice == 4:
        print(f"Result : {num1} ÷ {num2} = {num1/num2}")
