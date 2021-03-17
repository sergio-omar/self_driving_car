import cv2
import numpy as np

img = cv2.imread('road.jpg')
cv2.imshow('_', img)
cv2.waitKey(0)

y_size = img.shape[0]
x_size = img.shape[1]

color_select = np.copy(img)
line_image = np.copy(img)

#define the color criteria
red_threshold = 0
blue_threshold  = 0
green_threshold = 0

rgb_threshold = [red_threshold,green_threshold,blue_threshold]

left_bottom = [0,530]
right_bottom = [900,300]
apex = [400,0]

fit_left = np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right = np.polyfit((right_bottom[0],apex[0],right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((left_bottom[0],ringht_bottom[0]),left_bottom[1],right_bottom[1]),1)

