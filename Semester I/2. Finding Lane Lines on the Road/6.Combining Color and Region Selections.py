#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22
# @Author  : Joe

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np

# read the image
image = mpimg.imread('test.png')

# get the x and y size and make two copies of the image
# one copy we'll extract only the pixels that meet our selection
# then we'll paint those pixels red in the original image to 
# see our selection overlaid on the original
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)
line_image = np.copy(image)
print(image.shape)
# define our color criteria
red_threshold =200/255.0
green_threshold = 200/255.0
blue_threshold = 200/255.0
rgb_threshold = [red_threshold,green_threshold,blue_threshold]

# define a trianle region of interest(roi)
# keep in mind the origin(x=0,y=0) is in the upper left in image processing
# 
left_bottom = [0, ysize -1]
right_bottom = [xsize-1, ysize-1]
apex = [475, 320]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0],apex[0]),(right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]),(left_bottom[1], right_bottom[1]),1)

# mask pixels below the threshold
color_threshold = (image[:,:,0] < rgb_threshold[0]) |\
	(image[:,:,1] < rgb_threshold[1]) |\
	(image[:,:,2] < rgb_threshold[2])

# find the region inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0,ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) &\
	(YY > (XX*fit_right[0] + fit_right[1])) &\
	(YY < (XX*fit_bottom[0] + fit_bottom[1]))

# mask color selection
color_select[color_threshold & ~region_thresholds] = [0,0,0,1]

# find where image is both colored right and in the region
line_image[(~color_threshold) & region_thresholds] = [1,0,0,1]

# display
plt.subplot(121)
plt.imshow(color_select)
plt.title('color_select')
plt.subplot(122)
plt.imshow(line_image)
plt.title("line_image")
plt.show()