import cv2
import numpy as np

im = cv2.imread('road.jpg')

y_size = im.shape[0]
x_size = im.shape[1]

region_select = np.copy(im)
print(y_size)
print(x_size)
left_bottom = [150,720]
right_bottom = [1100, 720]
apex = [640,400]

fit_left = np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right = np.polyfit((right_bottom[0],apex[0]), (right_bottom[1],apex[1]),1)
fit_bottom  = np.polyfit((left_bottom[0],right_bottom[0]),(left_bottom[1],right_bottom[1]),1)

XX,YY = np.meshgrid(np.arange(0,x_size),np.arange(0,y_size))
region_threshold = (YY > (XX*fit_left[0]+ fit_left[1])) &\
        (YY > (XX*fit_right[0] + fit_right[1])) & \
        (YY < (XX*fit_bottom[0] + fit_bottom[1]))

region_select[region_threshold] = [255,0,0]

cv2.imshow('_', region_select)
cv2.waitKey(0)
