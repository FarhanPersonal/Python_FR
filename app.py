# FR: need to import cv2 like below otherwise doesn't work
from cv2 import cv2 as cv   
import numpy as np

import matplotlib.pyplot as plt

insImage = cv.imread('data/Institute.jpg', 0)

henriImage = cv.imread('data/Henri.jpg', 0)

array = np.array([1,2,3])
print(array)

print(type(array))
print(type(insImage))