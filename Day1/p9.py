# List Operations Program – on

# Step 1: Create a list
numbers = [10, 20, 30, 40, 20]
print("Original List:", numbers)

# Step 2: Accessing elements
print("\nAccessing Elements:")
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Step 3: Modifying list (lists are mutable)
numbers[1] = 200  # replacing 20 with 200
print("\nAfter modification:", numbers)

# Step 4: Adding elements
numbers.append(50)  # adds at end
numbers.insert(2, 25)  # adds at given index
print("\nAfter adding elements:", numbers)

# Step 5: Removing elements
numbers.remove(20)  # removes first occurrence of 20
removed_item = numbers.pop(3)  # remove by index
print("\nAfter removing elements:", numbers)
print("Removed item using pop():", removed_item)

# Step 6: Searching elements
print("\nSearching:")
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# Step 7: Sorting list
numbers.sort()
print("\nAfter sorting:", numbers)

# Step 8: Reversing list
numbers.reverse()
print("\nAfter reversing:", numbers)

# Step 9: Looping through list
print("\nLooping through list:")
for num in numbers:
    print(num, end=" ")