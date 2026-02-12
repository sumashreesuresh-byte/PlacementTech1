#lists
'''
bag1=["apple","mango","watermelon","sweet"]
bag2=["apple","watermelon","grapes","mango","chips"]
newl=bag1+bag2

new1=sorted(set(newl))
print()
print(new1)
print()
'''

#Dictionary
'''
d={
    "name":"sumaa",
    "age":20,
    "USN":108
}

keys=d.keys()
values=d.values()
print(keys)
print(values)
print(d["name"])
print(d["age"])
print(d["USN"])
'''

#findin the frequency of elements in the string
#s=input("Enter the string:")
#freq={}
#for char in s:
#    freq[char]=freq.get(char,0)+1
#print(freq)

dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}   
dict3={**dict1,**dict2}
print("Merged Dictionary is= ",dict3)
swap_dict={v:k for k,v in dict1.items()}
print("Swaped Dictionary is= ",swap_dict)