passw = input("Enter valid password: ")

if len(passw) > 4 and passw[4].isdigit() and 1 <= int(passw[4]) <= 5:
    print("Valid Password")
else:
    print("Invalid!")
