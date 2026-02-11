tablename=int(input("Enter the table Name(ex. 5 table 4 table): "))
limit=int(input("Enter the Limit: "))

for i in range(1,limit+1):
    print(tablename ," x ",i ,"= ",tablename*i)