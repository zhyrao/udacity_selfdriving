from matplotlib import pyplot as plt 
from matplotlib import image as mpimg 
import numpy as np 

# Theory
	# 假设车上的相机是安装在固定的位置上的，
	# 那么车道线就总会在图像的某一些特定的区
	# 域内。这样处理也可以增加运行速度。

# Read in the Image and print some attribute
img = mpimg.imread('test.png')
print('This image is: ', type(img),
	' with dimensions: ', img.shape)

# Get out the x and y size and make a copy
ysize = img.shape[0]
xsize = img.shape[1]
region_select = np.copy(img)

# Define a triangle region of interest(ROI)
# 注意在图片的处理过程中，（0,0）点是在图像
# 的左上角位置。
left_bottom = [0, ysize-1]
right_bottom = [xsize-1, ysize-1]
apex = [xsize/2,ysize/2]

# Fit lines (y = Ax + b) to identify the 3 sided region of interest
# np.polyfit() returns the coefficients [A, B] of the fit
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Find the  region inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

# Color pixels red which are inside the region of interest
# 注意颜色的范围取值为[0-1]
region_select[region_thresholds] = [1, 0, 0, 1]

# Display the image
plt.imshow(region_select)
plt.show()