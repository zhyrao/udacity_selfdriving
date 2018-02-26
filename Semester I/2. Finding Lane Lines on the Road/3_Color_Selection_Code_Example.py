import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np 

# Read in the image and print out some stats
img = mpimg.imread('test.png')	# 注意matplotlib只能读入 png 格式的图片
print('This image is: ', type(img),
	      ' with dimensions: ', img.shape)

# Get the x and y size and make a copy of image
ysize = img.shape[0]
xsize = img.shape[1]

# Note: always make a copy rather than simply using "="
color_select = np.copy(img)

# Define color selection criteria 
# 注意：由于matplotlib读入后的像素被压缩
# 到0-1之间，所以需要对阈值也进行压缩
red_threshold = 200/255.
green_threshold = 200/255.
blue_threshold = 200/255.
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

print(img[:,:,0])
# Identify pixels below the threshold
thresholds = (img[:,:,0] < rgb_threshold[0]) \
			| (img[:,:,1] < rgb_threshold[1]) \
			| (img[:,:,2] < rgb_threshold[2])

# 注意此处对应为RGBA格式图片，所有后面必须要有
# 透明度的值。
color_select[thresholds] = [0,0,0,1]

# Display the  image
plt.imshow(color_select)
plt.show()