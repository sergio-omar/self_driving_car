import cv2
import numpy as np

img = cv2.imread('road.jpg')

y_size = img.shape[0]
x_size = img.shape[1]
print(y_size)
print(x_size)
color_select = np.copy(img)
line_image = np.copy(img)

#define the color criteria
red_threshold = 220
blue_threshold  = 220
green_threshold = 220

rgb_threshold = [red_threshold,green_threshold,blue_threshold]
#this are the three points that define the poligon
left_bottom = [180,720]
right_bottom = [1100,720]
apex = [x_size/2,300]

#Polyfit returns an array of deg+1 length that represents the coefficients of
#polynom
fit_left = np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right = np.polyfit((right_bottom[0],apex[0]),(right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((left_bottom[0],right_bottom[0]),(left_bottom[1],right_bottom[1]),1)

#this nex line check every pixel if is lower than the threshold, for the
#the three channels, and generate a matrix of the width and length of the 
#picture with true and false. True if any of the 3 channels is higher than
# thre threshold
color_thresholds = (img[:,:,0] < rgb_threshold[0]) | \
                    (img[:,:,1] < rgb_threshold[1]) | \
                    (img[:,:,2] < rgb_threshold[2])

#meshgrid return two weird  arrays.
XX, YY = np.meshgrid(np.arange(0, x_size), np.arange(0, y_size))

#region threshold will be a matrix of true and false telling us where is the
#area of interest. xx*fit_left[0]+fit_left[1]  (its the linear equation that
#separates the non interest area from INterest area)
#(NOTE IN ANY MOMENT A TRIANGLE WAS "IMPLICITLY" CONSTRUCTED)
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
print("this is region_thresholds")
print(region_thresholds.shape)

color_select[color_thresholds] = [0,0,0]

#This line its really interesting, this will take the two arrays
#and compare it one by one with its corresponding match
# from one array we have the color thresholds vs region thresholds
#if the both are true will take the [x,y,z] color.

line_image[~color_thresholds & region_thresholds] = [0,255,0]

#finally display the image with the selected lane lines
cv2.imshow('_',line_image)
cv2.waitKey(0)
