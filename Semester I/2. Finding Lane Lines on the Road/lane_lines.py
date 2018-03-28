from matplotlib import pyplot as plt 
import numpy as np 
import cv2 as cv

cap = cv.VideoCapture('test.mp4')

while True:
	ret, frame = cap.read()

	if ret == False:
		break

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	kernel_size = 5
	blur_gray = cv.GaussianBlur(gray, (kernel_size,kernel_size), 0)

	l_thres = 50
	h_thres = 150
	edges = cv.Canny(blur_gray, l_thres, h_thres)
	

	mask = np.zeros_like(edges)
	ignore_mask_color = 255

	imshape = frame.shape
	vertices = np.array([[(200,imshape[0]-100), (imshape[1]/2 -100,imshape[0]/2+100),
		 (imshape[1]/2+100, imshape[0]/2+100),(imshape[1]-200, imshape[0]-100)]], dtype = np.int32)
	cv.fillPoly(mask, vertices, ignore_mask_color)
	masked_edges = cv.bitwise_and(edges, mask)
	cv.imshow('masked_edges',masked_edges)

	rho = 2
	theta = np.pi/180
	threshold = 15
	min_line_length = 80
	max_line_gap = 50

	lines = cv.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
		min_line_length,max_line_gap)

	if lines is not None:	
		for line in lines:
			for x1,y1,x2,y2 in line:
				cv.line(frame,(x1,y1),(x2,y2),(255,0,0),2)

	cv.imshow('frame',frame)

	k = cv.waitKey(60) & 0xff
	if k == 27:
		break

cap.release()
cv.destroyAllWindows()