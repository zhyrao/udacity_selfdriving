##### Using the Hough Transform to Find Lines from Canny Edges
    在图像空间中，一条线被表示为x,y点的集合，但是在1962年，Paul Hough设计了  
    一个新的方式，参数空间，来表达线，为了纪念他，我们都称为"Hough Space",  
    霍夫空间。    

    在霍夫空间中，我们可以将直线 L 的x,y方式改为m,b方式来表示。
$$y = mx + b$$
    
    霍夫变换就是指从图像空间转换为霍夫空间的过程。所以，在图像空间中表示直线的  
    将在霍夫空间中表示为一个点(m,b)

-------------
![Hough Space](https://github.com/zhyrao/udacity_selfdriving/blob/master/Image/hough_1.jpg?raw=true)        
    
     如果在图像空间中的一条线对应在霍夫空间上是一个点，那么在图像空间中的两条  
     平行的线对应在霍夫空间中是什么么？
- [ ] A
- [x] B
- [ ] C
- [ ] D

-------
![Hough Space](https://github.com/zhyrao/udacity_selfdriving/blob/master/Image/hough_2.jpg?raw=true)
    
    好了，如果在图像空间中一条线对应在霍夫空间中是一个点，那么在图像空间中的一  
    个点对应在霍夫空间中是什么呢？
- [x] A
- [ ] B
- [ ] C
- [ ] D

-------
![Hough Space](https://github.com/zhyrao/udacity_selfdriving/blob/master/Image/hough_3.jpg?raw=true)

    如果在图像空间中有两个点，那么在霍夫空间中看起来是什么样的呢？
- [ ] A
- [ ] B
- [x] C
- [ ] D
     
---
![Hough Space](https://github.com/zhyrao/udacity_selfdriving/blob/master/Image/hough_4.jpg?raw=true)

    现在我们在霍夫空间中有两条相交的线，那么在图像空间中他们的交点是怎么样的呢？
- [x] 一条同时通过(x1,y1)和(x2,y2)的直线
- [ ] 图像空间中,在(x1,y1)和(x2,y2)之间的直线
- [ ] 通过(x1,y1)的直线
- [ ] 通过(x2,y2)的直线

---
![Hough Space](https://github.com/zhyrao/udacity_selfdriving/blob/master/Image/hough_5.jpg?raw=true)

    如果我们对图像空间中的正方形进行霍夫变换，会发生什么样的变化呢？
- [ ] A
- [ ] B
- [x] C
- [ ] D


