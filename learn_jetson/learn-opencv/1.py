import cv2 as cv
print(cv.__version__)

import numpy as np
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot open camera")
    exit()

while True:
    # 逐帧捕获
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame. exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
