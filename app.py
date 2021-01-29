import numpy
import numpy
from scipy import interpolate

x_coord = [0, 1, 0, 1]
z_coord = [0, 0, 1, 1]

y_displ = [1, 7, 5, 1]

row_wise_data = tuple(zip(x_coord, z_coord, y_displ))


def get_array_from_tuple(data_tuple, col_indx_in_tuple):
    data_array = []
    for i in range(0, len(data_tuple)):
        data_array.append(data_tuple[i][col_indx_in_tuple])

    return data_array


# getting back y_displ array:
x_coord_array = get_array_from_tuple(row_wise_data, 2)

print(x_coord_array)
