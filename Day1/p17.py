import pandas as pd 
df=pd.read_csv('t1.txt')
print(df)

print(df['Name'])
print(df['Marks'])
print(df['Marks'].max())
print(df['Marks'].min())
print(df['Marks'].sum())

print("retrive wiht condition")

greater_than_80=df[df['Marks']>98]
print(greater_than_80)


print("--------graph--------")
import matplotlib.pyplot as plt

print("----------graph-------")
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()