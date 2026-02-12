# The data is provided as a set, and you need to identify the highest and lowest fuel efficiency values to help the company make data-driven decisions.


# Read input values
n = int(input("Enter the number of vehicles: "))    
efficiency = []
print("Enter the fuel efficiency values:")
for i in range(n):
    value = float(input())
    efficiency.append(value)
# Find the highest and lowest fuel efficiency
highest_efficiency = max(efficiency)
lowest_efficiency = min(efficiency)
# Print the results
print(f"Highest fuel efficiency: {highest_efficiency}")
print(f"Lowest fuel efficiency: {lowest_efficiency}")
