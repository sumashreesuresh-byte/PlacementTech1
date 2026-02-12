# ==============================================================
#                     PYTHON INPUT
# ==============================================================

# INTRODUCTION:
# The input() function in Python is used to take input from the user.
# Whatever the user types → comes as a STRING by default.


# ==============================================================
# 1) BASIC INPUT
# ==============================================================

# SYNTAX:
# value = input("Enter something: ")

name = input("Enter your name: ")
print("Hello,", name)


# ==============================================================
# 2) TAKING INTEGER INPUT
# ==============================================================

# input() returns string → must convert to int

age = int(input("Enter your age: "))
print("You are", age, "years old.")


# ==============================================================
# 3) TAKING FLOAT INPUT
# ==============================================================

price = float(input("Enter price: "))
print("Final Price =", price)


# ==============================================================
# 4) TAKING MULTIPLE INPUTS IN ONE LINE (split)
# ==============================================================

# split() → breaks the input based on spaces  
# map() → converts each value into desired type  

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# Example:
# Input: 10 20
# Output: 30


# ==============================================================
# 5) TAKING LIST INPUT
# ==============================================================

# List of integers
nums = list(map(int, input("Enter numbers: ").split()))
print(nums)

# Example Input: 10 20 30 40
# Output: [10, 20, 30, 40]

# List of strings
words = input("Enter words: ").split()
print(words)


# ==============================================================
# 6) TAKING COMMA-SEPARATED INPUT
# ==============================================================

# Split by comma → .split(",")

data = input("Enter values: ").split(",")
print(data)

# Example Input: a,b,c
# Output: ['a', 'b', 'c']


# ==============================================================
# 7) ADVANCED: EVAL() FUNCTION
# ==============================================================

# eval() → evaluates expression as Python code  
# ⚠️ Not safe for real applications

x = eval("10 + 20")
print(x)  # Output: 30

expr = input("Enter expression (ex: 10+5*2): ")
result = eval(expr)
print("Result =", result)

# Evaluating list
lst = eval(input("Enter a list: "))
print(lst)


# ==============================================================
# 8) USING input() WITH CONDITIONALS
# ==============================================================

name = input("Enter name: ")
if name == "admin":
    print("Welcome Admin!")
else:
    print("Hello User!")


# ==============================================================
# 9) USING strip(), lstrip(), rstrip()
# ==============================================================

# strip()  → removes spaces from both sides  
# lstrip() → removes spaces from left  
# rstrip() → removes spaces from right  

text = "   hello world   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ==============================================================
# 10) STRING INPUT CLEANING
# ==============================================================

# lower()  → convert to lowercase  
# upper()  → convert to uppercase  
# title()  → first letter capital  

s = input("Enter text: ").lower()
print("Cleaned text =", s)


# ==============================================================
# 11) JOIN FUNCTION (opposite of split)
# ==============================================================

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)


# ==============================================================
# 12) REPLACE FUNCTION
# ==============================================================

text = "I like Java"
text = text.replace("Java", "Python")
print(text)


# ==============================================================
# 13) CHECK FUNCTIONS
# ==============================================================

# isalpha()   → a-z only
# isnumeric() → 0-9 only
# isalnum()   → a-z + 0-9

s = input("Enter string: ")

print(s.isalpha())
print(s.isnumeric())
print(s.isalnum())


# ==============================================================
# 14) FULL PROGRAM USING EVERYTHING
# ==============================================================

# Take name, marks and calculate average

name = input("Enter your name: ").title()
marks = list(map(int, input("Enter marks: ").split()))

average = sum(marks) / len(marks)

print("Student:", name)
print("Marks:", marks)
print("Average =", average)
