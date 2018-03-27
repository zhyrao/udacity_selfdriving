#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27
# @Author  : Joe

# 现在我们已经知道了霍夫变换工作的原理，但是去完成找到车道线的这个目标，
# 我们还需要去指定一些参数来说明我们想检测什么样类型的车道线（例如，长的
# 车道线，短的车道线，弯曲的车道线，连续的车道线等等）。

# 这里，我们需要使用Opencv中的函数HoughLinesP并设定它的一些参数信息。现
# 在我们来了解一下我们将要使用到的函数HoughLinesP的参数信息等。
	# lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([])
	# min_line_length, max_line_gap)
# 在这里，我们是在masked_edges（Canny的返回）图像上操作的，并且从HoughLinesP
# 返回的就是lines，它是一个由变换操作检测到的包含所有线段的两个端点(x1,y1,x2,
# y2)的数组。其他的参数定义了我们想要检测的线段的类型。

# 首先， rho 和theta是霍夫空间中我们网格对应的距离和角度。记住，在霍夫空间中，
# 我们有一个从（Θ, ρ）轴延展的网格。我们需要指定rho像素单位和theta的弧度单位。

# 参数threshold指定了最小的投票数量。空的np.array([])只是一个占位器，不需要
# 去改变它。min_line_length是能够接受的最短的线段距离，max_line_gap是两条线
# 段之间最大的距离，如果他们小于这个距离可以被认为是一条线段连接起来。最后可以
# 迭代输出lines并且在图像中显示出来

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np
import cv2

# read in and grayscale the image
image = cv2.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# define our parameters for canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold,high_threshold)

# define the hough transform parameters
# make a blank the same size as our image to draw on
rho = 1
theta = np.pi/180
threshold = 20
min_line_length = 150
max_line_gap = 10
line_image = np.copy(image)*0

# run hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# draw
for line in lines:
	for x1,y1,x2,y2 in line:
		cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 2)

# create a 'color' binary image to  combine with line image
color_edges = np.dstack((edges, edges, edges))

# draw the line on the edge image
combo = cv2.addWeighted(image, 0.8, line_image, 1, 0)

cv2.imshow('combo', combo)

cv2.waitKey(0)
cv2.destroyAllWindows()
