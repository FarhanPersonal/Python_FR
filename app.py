# FR: need to import cv2 like below otherwise doesn't work
from cv2 import cv2 as cv   
import numpy as np

import matplotlib.pyplot as plt

# convert obtained color image to grey image by setting flag = 0
insImage_grey = cv.imread('data/Institute.jpg', 0)


# See the size of the insImage which is a color image
cv.imshow('image', insImage_grey)
cv.waitKey(0)


# print(type(insImage))

# See the size of the henriImage which is a greyscale image
henriImage = cv.imread('data/Henri.jpg', 0)


