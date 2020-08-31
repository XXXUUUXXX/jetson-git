'''
创建一个黑色图像
从左上角到右下角绘制一条蓝线
在右上角画一个绿色矩形
在矩形里画圆
画椭圆
画多边形
添加文本
'''

import numpy as np
import cv2 as cv

print(cv.__version__)

img = np.zeros((512,512,3), np.uint8) # 创建黑色图像
# (坐标，颜色，厚度)
# 从左上角到右下角绘制一条蓝线
cv.line(img, (0,0), (511,511), (255,0,0), 5) 
# 在右上角画一个绿色矩形
cv.rectangle(img, (384,0), (510,128), (0,255,0), 3)
# 在矩形里画圆
cv.circle(img, (447,63), 63, (0,0,255), -1)
# 画椭圆
cv.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)
# 画多边形
pts = np.array([[10,5], [20,30], [70,20],[50,10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0,255,255))
# 添加文本
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'opencv', (10,500), font, 4, (255,255,255), 2, cv.LINE_AA)

cv.imwrite('black.jpg', img)
