stry=input("Enter a string value:\n")
capi=stry.capitalize()
rev=stry[::-1]
cap1=stry.title()
cc=0
v="AEIOUaeiou"
vc=0
for char in stry:
    if char in v:
        vc+=1
nv=""
for char in stry:
    if char not in v:
        nv+=char
print("Capilalized string= ", capi)
print("Capilalized first word= ", cap1)
print("reverse string= ", rev)
print("Number of vowels= ", vc)
print("String without vowels= ", nv)
if stry==rev:
    print("String is palindrome")
else:
    print("String is not palindrome")

ch=input("Enter which char to count its occurance: ")
cc=stry.count(ch)
print("Number of times", ch, "occured is", cc)