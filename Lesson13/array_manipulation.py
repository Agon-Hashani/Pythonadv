import numpy as np

# arr_2d = np.array([[[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]],[[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]]])
arr_2d = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
#
# print(arr_2d)

# element = arr_2d[1, 2]
# print(element)
#
# dim = arr_2d.ndim
# print(dim)

# arr_shape = arr_2d.shape
# print(arr_shape)

# arr_size = arr_2d.size
# print(arr_size)

# sub_arr = arr_2d[:2, :2]
# # print(sub_arr)

# sub_array_3 = arr_2d[-4:, -4:]
# print(sub_array_3)

# sub_array_4 = arr_2d[:, ::2]
# print(sub_array_4)

# total_sum = np.sum(arr_2d)
# print(total_sum)

# mean = np.mean(arr_2d)
# print(mean)

# sum_cols =np.sum(arr_2d, axis=0)
# print(sum_cols)

# sum_rows =np.sum(arr_2d, axis=1)
# print(sum_rows)

reshaped_arr = arr_2d.reshape(((5,2)))#4
print(reshaped_arr)