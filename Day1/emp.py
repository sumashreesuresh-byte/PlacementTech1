import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("empdata.csv")

# Display first and last rows
print(df.head())
print(df.tail(3))
print(df.shape)

# Average salary
avg_salary = df["Salary"].mean()
print("Average Salary =", avg_salary)

# Highest salary employee
max_salary = df["Salary"].max()
max_emp = df[df["Salary"] == max_salary]
print("Highest Salary Employee:")
print(max_emp)

# Lowest salary employee
min_salary = df["Salary"].min()
min_emp = df[df["Salary"] == min_salary]
print("Lowest Salary Employee:")
print(min_emp)

# Employees per department
dept_count = df["Department"].value_counts()
print("Employees per department:")
print(dept_count)

# Filtering examples
high_salary = df[df["Salary"] > 50000]
print("Employees with salary > 50000:")
print(high_salary)

# Grouping example
avg_dept_salary = df.groupby("Department")["Salary"].mean()
print("Average salary per department:")
print(avg_dept_salary)

# Create Salary Status column
df["Salary Status"] = df["Salary"].apply(
    lambda x: "High" if x > 50000 else "Low"
)

# Seniority column
def seniority(exp):
    if exp >= 10:
        return "Senior"
    elif exp >= 5:
        return "Mid"
    else:
        return "Junior"

df["Seniority"] = df["Experience"].apply(seniority)

print(df)

# Simple Bar Chart
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# Save high salary employees
high_salary.to_csv("high_salary.csv", index=False)

print("DONEEEEE 😤🔥")
