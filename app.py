# FR: need to import cv2 like below otherwise doesn't work
from cv2 import cv2 as cv   
import numpy as np

import matplotlib.pyplot as plt

insImage = cv.imread('data/Institute.jpg')
# See the size of the insImage which is a color image
print("Shape of insImage obtained through imread is ", insImage.shape)

# See the size of the henriImage which is a greyscale image
henriImage = cv.imread('data/Henri.jpg', 0)
print("Shape of henriImage obtained through imread is ", henriImage.shape)


array1 = np.zeros((3,4), dtype=int)

array2 = np.ones((3,4), dtype=int)

# creating array with a specific number
array3 = np.full((3,4), 5, dtype=int)

# creating array with random number
array_random = np.random.random((3,4))

print(array1)
print(array2)
print(array3)
print(array_random)

print(type(np))
print(type(np.random))
print(type(np.random.random()))



