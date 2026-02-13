
import numpy as np

a=np.array([[1,2,3],
           [1,4,6],
           [7,8,9]])
print(a)
print(a)
print(a.shape)
print(type(a))
print(np.sum(a))

aa=np.zeros((2,2))
print(aa)

aa=np.ones((4,7))
print(aa)
aa=np.full((3, 3), 5)
print(aa)
aa=np.random.random((3, 3)) 
print(aa)
d=np.eye(4)
print(d)

f=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
print(a.shape)
print(a[0])
print(a[1][2])
a[1][2]=100
print(a)
print(a[1][2])

print(np.count_nonzero(a))
print("--indexing--")
sub_arry=a[1:3,0:2]
print(sub_arry)


#seat booking system
seats = np.zeros((10, 10), dtype=int)
seats[0][1] = 1
seats[2][3] = 1
seats[2][5] = 1
seats[4][4] = 1
seats[7][8] = 1

print("Seat Matrix:\n", seats)
total_booked = np.sum(seats)
print("Total booked seats:", total_booked)

third_row_booked = np.sum(seats[2])
print("Booked seats in 3rd row:", third_row_booked)
