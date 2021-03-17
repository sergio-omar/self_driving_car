import cv2
import numpy as np

img = cv2.imread('road.jpg')
print(img.shape)
y_size = img.shape[0]
x_size = img.shape[1]
print(y_size)
print(x_size)

color_select = np.copy(img)

red_threshold = 200
green_threshold = 200
blue_threshold = 200

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

threshold = ((img[:,:,0] < rgb_threshold[0]) \
        | (img[:,:,1] < rgb_threshold[1]) \
        | (img[:,:,2] < rgb_threshold[2]))

color_select[threshold] = [0,0,0]
cv2.imshow('color_select',color_select)
cv2.waitKey(0)


