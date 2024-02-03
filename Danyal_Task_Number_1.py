# DANYAL ABBAS
# N/A
# gamingindustry9@gmail.com

"""1. Even or Odd Checker:"""

num = int(input("Write a number: "))
if num%2:
    print(f"{num} is a odd number")
else:
    print(f"{num} is a even number")


"""2. Multiplication Table Generator:"""

table = int(input("Write a number you want the table of : "))
for i in range(1,11):
    print(f"{table} x {i} = {table*i}")


"""3. Factorial Calculator:"""

fact = int(input("Write a number you want the factorial of : "))
number = 1
for i in range(1,fact+1):
    number *= i
print(f"{number} is the factorial of {fact}")


"""4. Sum of Digits:"""

n = input("write a number: ")
add = 0
for i in n:
    add += int(i)
print(f"The addition of the numbers is: {add}")


"""5. FizzBuzz Game:"""

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print(f"{i} : FizzBuzz")
    elif i%3 == 0:
        print(f"{i} : Fizz")
    elif i%5 == 0:
        print(f"{i} : Buzz")
    else:
        print(i)


"""6. Palindrome Checker:"""

palin = input("Write a word: ")
if palin == palin[::-1]:
    print(f"{palin} is a palindrome")
else:
    print(f"{palin} is not a palindrome")


"""7. Prime Number Checker:"""

prime = int(input("Write a number: "))
l = []
for i in range(2, prime//2):
    if prime%i==0:
        l.append(False)
    else:
        l.append(True)
if all(l):
    print(f"{prime} is a prime number")
else:
    print(f"{prime} is not a prime number")


"""8. Guess the Word Game:"""

import random

words = ["damn", "me", "actually", "want", "to", "kms","right", "now"]
word = random.choice(words)

smt = ""
while True:
    for i in word:
        if i in smt:
            print(i,end="")
        else:
            print("_", end="")
    
    if word == smt:
        print("\n\nYOOO!! YOU GUESSED THE WORD!!")
        break
        
    guess = input("\n\nGuess the word, only one letter allowed: ")
    

    if len(guess) == 1:
        if guess in word:
            smt += guess
            continue
        else:
            pass
    else:
        print("Only one letter at a time G")
        continue






