import numpy as np

# Creating Arrays ex1
# Ex 1 -1
x = np.diag(np.array([1, 1, 1, 1]))
# Ex 1 -2
matrix2 = np.zeros((4, 5))
# random -1
matrix_rondom1 = np.random.rand(20)
# random -2
matrix_rondom2 = np.linspace(0, 1, 20)
# random -4
matrix_rondom3 = np.random.randint(low=10, high=20, size=20)
# ranges-1
ranges1 = np.arange(10, 20, 2)
# ranges-2
ranges2 = np.arange(10).reshape(2, 5)
# Dimensions
dimensions1 = np.random.rand(3, 4, 2)
# Accessing Values
matrix3 = np.random.randint(50, 100, 25).reshape(5, 5)
# Ex 1 -1
last_num = matrix3[-1][-1]
# Ex 1 -2
num_2_3 = matrix3[1][2]
# Ex 1 -3
tow_value = matrix3[0][1:3]
# Ex 1 -4
tow_value2 = matrix3[-2][[0, 3]]
# Ex 1 -5
num_4row_3 = matrix3[3][:3]
# Ex 2
matrix_3 = matrix3 = np.random.randint(1, 50, 50).reshape(5, 10)
# Ex 2-1
secount_row = matrix_3[1]
# Ex 2-2
first_last_row = matrix_3[[0, -1],]
# Ex 2-3
last_3_rows = matrix_3[-3:]
# Ex 2-4
values = matrix_3[[0, 2, 4], :2]
# Ex 2-5
values_all_row = matrix_3[:, [1, -1]]

# Updating Arrays
# Ex 1 -1
matrix_ex1 = np.ones((3, 6))
# Ex 1 -2
matrix_ex1[-2] = 2
# Ex 1 -3
matrix_ex1[:2, :2] = 0
# Ex 1 -4
matrix_ex1[:, [3, 4]] = 5

# Ex 2 -1
matrix = np.random.randint(1, 11, 18).reshape(3, 3, 2)
# Ex 2 -2
matrix[:, :, 1] = -1

# Swap
matrix = np.random.randint(25, 49, 25).reshape(5, 5)
# Swap -1
matrix[:, [1, 2]] = matrix[:, [2, 1]]
# Swap -2
matrix[[0, -1], :] = matrix[[-1, 0], :]
# Ex 2
matrix = np.random.uniform(5, 10, [4, 4])
