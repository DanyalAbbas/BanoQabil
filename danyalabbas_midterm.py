# Danyal Abbas
# Midterm Examination

# Q1 - Write a Python program to do arithmetical operations addition and division.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

add = num1 + num2
div = num2/num1

print(f"The addition of {num1} and {num2} is {add}")
print(f"The division between {num2} and {num1} is {div}")


# Q2 - Write a Python program to find the area of a triangle

base = int(input("Enter the base of the triangle: "))
perp = int(input("Enter the perp of the triangle: "))
area = 0.5*base*perp

print(f" The area of triangle is {area}")

# Q3 - Write a Python program to convert Celsius to Fahrenheit.

celcius = float(input("Enter the temperuter in celsius: "))
fahren = (9/5)*celcius + 32
print(f"The temperature in fahrenheit is: {fahren}")

# Q4 - Write a Python program that return all datatypes that we discussed in the class.

num = 15
fl = 6.9
s = "Danyal"
bl = True

print(f"\n The datatype of {num} is {type(num)}")
print(f"The datatype of {fl} is {type(fl)}")
print(f"The datatype of {s} is {type(s)}")
print(f"The datatype of {bl} is {type(bl)}")