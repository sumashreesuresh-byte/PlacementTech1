#Eception handling in python
'''
print("wake up")
print("get ready")
print("drive for ",int(10/2),"km")
try:
    print(2/0)
except ZeroDivisionError:
    print("cannot divide by zero")
print("reach college")
print("listen to the lecture")
'''
'''
numbers=[1,2,3,0,"hi",8]
for num in numbers:
    try:
        result=10/num
        print(f"result: ",{result})
    except ZeroDivisionError:
        print("Error: Exception occurred while dividing by zero")
    except Exception as e:
        print("Unknown error occurred: ",e)
    finally:
        print("Thank you")
'''
'''
#Throwing an exception
def validateage(age):
    if age<18:
        raise ValueError("Invalid age")
    else:
        print("Elegible")
try:
    validateage(int(input("Enter the age to check: ")))
except Exception as e:
    print(e)

class LessAgeException(Exception):
    pass
class MoreAgeException(Exception):
    pass    

#custom exception
def validateage(age):
    if age < 18:
        raise LessAgeException("Age is less than 18")
    elif age > 60:
        raise MoreAgeException("Age is greater than 60")
    else:
        print("Eligible")
try:
    validateage(int(input("Enter the age to check: ")))
except LessAgeException as l:
    print(l)
except MoreAgeException as m:
    print(m)
'''

#Problem 1: take first and last name form user and cfraete a valid method
#validtion rule:
#a. first name and lastename length must be more than 3
#b. both fname and lname must have only characters
#if any of the conditions fail raise exception custom exception with appropriate message
class InvalidNameException(Exception):
    pass
def validate_name(fname,lname):
    if len(fname)<=3 or len(lname)<=3:
        raise InvalidNameException("Length of fname or lname must be more than 3")
    if not fname.isalpha() or not lname.isalpha():
        raise InvalidNameException("Only characters are allowed")
    return True
try:
    fname=input("Enter first name: ")
    lname=input("Enter last name: ")
    if validate_name(fname,lname):
        print("Valid Name")
except InvalidNameException as e:
    print(e)
