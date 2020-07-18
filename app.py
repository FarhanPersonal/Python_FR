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


array = np.array([1,2,3])
# print(array)

print(type(array))
print(type(insImage))
# print("Shape of array is ", array.shape)