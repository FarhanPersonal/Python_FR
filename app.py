import numpy
import numpy
from scipy import interpolate

x_coord = [0, 1, 0, 1]
z_coord = [0, 0, 1, 1]

y_displ = [1, 7, 5, 1]

x_coord_2d = numpy.reshape(x_coord, (2, 2))
z_coord_2d = numpy.reshape(z_coord, (2, 2))

y_displ_2d = numpy.reshape(y_displ, (2, 2))

# need to know y_dipl at location x_coord = 0.5, y_coord = 0.5 (say)

x_coord_new = 0.5
z_coord_new = 0.5

# get interpolation function
interpolation_output_func = interpolate.interp2d(
    x_coord_2d, z_coord_2d, y_displ_2d, kind='linear')

# get value of
y_displ_interpolated = interpolation_output_func(x_coord_new, z_coord_new)

print(y_displ_interpolated[0])
