"""
从摄像机捕获，沿垂直方向翻转每一帧并保存
"""

import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("can't receive frame (stream end?). exiting...")
        break
    frame = cv.flip(frame, 0)
    out.write(frame) # 写翻转的框架
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# 释放
cam.release()
out.release()
cv.destroyAllWindows()


