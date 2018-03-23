#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-23
# @Author  : Joe

# Canny Edge Detection
# 现在我们对Canny Edge Detection算法有了一个初步的概念了，
# 是时候来采用这个算法在图像中监测其中的车道线了。

# 首先，我们需要读取一副图像
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
image = mpimg.imread('exit-ramp.jpg')
plt.subplot(131)
plt.imshow(image)
plt.title('origin')

# 现在我们有一张道路的图像，很容易用肉眼可以看出其中的车道线
# 在哪里，那么如果用计算机视觉呢？

# 我们继续将它转换为灰度图
import cv2 # bringing in opencv libraries
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.subplot(132)
plt.imshow(gray, 'gray')
plt.title('gray')
#plt.show()

# 让我们在这幅图像中试试Canny Edge Detector。这就是opencv起作用
# 的地方。首先我们来看看OpenCV中函数Canny的参数：
	# edges = cv2.Canny(gray, low_threshold, high_threshold)
# 在这种情况下，在图像gray上面进行canny算法，并且返回输出的图像是
# 另外一个叫edges的图像。low_threshold和high_threshold是用来检测
# 边界的阈值。

# 这个算法会首先监测高于high_threshold强的边界（强的梯度变化），然
# 后排除掉那些低于low_threshold的像素。下一步，在high_threshold和
# low_threshold阈值之间的像素值会依据它们是否和高边界像素连在一起而
# 决定是否保留。输出的图像edges是二值化图像,  其中白色的像素代表了监测
# 到的边界信息，其他的非边界都是黑色的。详细信息查阅Opencv Canny文档。

# 那么这些参数的合理的取值范围是多少呢？在我们的情况中，当转为灰度图
# 以后，灰度图是一副8位的图像。所以每个像素可以使 2^8 = 256 个值，也就
# 是取值范围是0到255

# 这个范围意味着导数将会是十或者百的比例内。对于low_threshold和high_
# threshold的比例，Jhon Canny本人推荐它们的比例是1:2或者1:3 。

# 我们也会在应用canny算法之间对图像使用gaussian模糊处理，这个的好处是
# 可以降低噪声以及可以平滑图像中的梯度过度。cv2.Canny()函数实际上在内
# 部实现了高斯模糊，但是我们在这里也要做处理是因为可以应用更深层次的平
# 滑处理而得到不同的结果。

# 可以为高斯平滑处理选择任意奇数的kernel_size。一个大的kernel_size会
# 对一个较大范围内做处理。
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# 这里的处理是因为matplotlib读入的图像的像素值是在范围0-1之间的
# 所以需要在canny之间缩放2^8倍。

#blur_gray = np.uint8(blur_gray* 256) 
# print(blur_gray)
# print(blur_gray.dtype)
# print(cv2.__version__)

# cv2.imshow('blur_gray', blur_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# define parameters for canny 
low_threshold = 50
high_threshold = 200
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# display
plt.subplot(133)
plt.imshow(edges, cmap='gray')
plt.title('edges')
plt.show()