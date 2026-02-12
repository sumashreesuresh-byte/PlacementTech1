n = int(input("Enter the number of elements in the array\n"))

n = []

print("Enter the elements in the array")
for i in range(n):
    num = int(input())
    n.append(num)

freq = {}

for num in n:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.values())

if max_freq == 1:
    print("The mode of the array is none")
else:
    for key in freq:
        if freq[key] == max_freq:
            print("The mode of the array is")
            print(key)
            break
