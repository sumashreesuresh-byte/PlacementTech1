#input 3 tuples and find the multiplication in the kth coulmn
k = int(input("Enter the column number to multiply (1, 2, 3,.....): "))

tuples = []
for i in range(3):
    tuple_input = input(f"Enter tuple {i + 1} (comma-separated values): ")
    tuple_values = tuple(map(int, tuple_input.split(',')))
    tuples.append(tuple_values)
    
result = 1
for t in tuples:
    result *= t[k - 1]
    
print(f"The multiplication of the values in column {k} is: {result}")
