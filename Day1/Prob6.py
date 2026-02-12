# to count how many scores are even and how many are odd
nums=input("Enter the scores with spaces: \n")
nu=[]

for i in nums.split():
    nu.append(int(i))

ec=0
eo=0

for i in nu:
    if i%2==0:
        ec+=1
    else:
        eo+=1

print("Even count is",ec)
print("Odd count is",eo)