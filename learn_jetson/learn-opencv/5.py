"""
轨迹栏做成调色板子
"""


import numpy as np
# import cv2 as cv
# from cv2 import cv2
# from cv2 import cv2
# 或者
import cv2.cv2 as cv


def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8) # 创建黑色图像，窗口
cv.nameWindow('image')

# 创建颜色变化轨迹栏
cv2.from django.conf import setting