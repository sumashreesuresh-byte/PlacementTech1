#Second largest element in an array
n=int(input("Enter the number of elements in the array\n"))
arr = []
print("Enter the elements in the array")
for i in range(n):
    num = int(input())
    arr.append(num)

largest = second_largest = float('-inf')
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print("The second largest element in the array is", second_largest)
    
