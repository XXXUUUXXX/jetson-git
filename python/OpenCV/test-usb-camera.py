import cv2 as cv
import numpy as np
import time


print(cv.__version__)

timeMark = time.time() # 时间标记
dtFIL = 0       # 低通滤波，表示时间变化
width = 640     # 800 640 1280 1920
height = 480    # 600 480 720  1080
flip=2          # 设置翻转
font = cv.FONT_HERSHEY_SIMPLEX # 设置字体

# G streamer 是从摄像机源到显示器源的通道

# 树莓派摄像头捕获,用！隔开命令;
# flip-method=2正常，flip-method=0表示反转图像
# wbmode表示白平衡模式，通过gst-inspect-1.0 nvarguscamerasrc命令查看
# tnr为temporal noise reduction时间噪声降低
# tnr-mode表示时间噪声降低模式，通过gst-inspect-1.0 nvarguscamerasrc命令查看
# tnr-strength表示时间降噪强度，通过gst-inspect-1.0 nvarguscamerasrc命令查看
# ee-mode表示边缘模式，通过gst-inspect-1.0 nvarguscamerasrc命令查看
# ee-strength表示边缘增强强度，通过gst-inspect-1.0 nvarguscamerasrc命令查看
# videobalance表示视频平衡， contrast表示对比度，通过gst-inspect-1.0 videobalance命令查看
# brightness表示亮度，通过gst-inspect-1.0 videobalance命令查看
# saturation表示饱和度，，通过gst-inspect-1.0 videobalance命令查看
# camSet = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=‘+str(flip)+’ ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink' 

# drop=True 可以消除延迟
# camSet1 = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=3 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=‘+str(flip)+’ ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.15 saturation=1.2 ! appsink drop=True' 
# camSet2 = 'nvarguscamerasrc sensor-id=1 ee-mode=2 ee-strength=0 tnr-mode=3 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=‘+str(flip)+’ ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.15 saturation=1.2 ! appsink drop=True' 

# cam1 = cv.VideoCapture(camSet1)
# cam2 = cv.VideoCapture(camSet2)
# USB摄像头捕获
# 方法一
cam3 = cv.VideoCapture('/dev/video0') 
# 方法二，没成功运行
# camSet = 'v4l2src device=/dev/video0 ! video/x-raw, width='+str(width)+', height='+str(height)+', framerate=25/1 ! videoconvert ! appsink'
# cam = cv.VideoCapture(camSet)

while True:
    # _, frame1 = cam1.read()
    # _, frame2 = cam2.read()
    _, frame3 = cam3.read()

    # frame3 = np.hstack((frame1, frame2)) # 组合框架1和2
    dt = time.time() - timeMark          # 时间种子
    timeMark = time.time()               # 新的时间标记
    dtFIL = .9*dtFIL + .1*dt             # 低通滤波
    fps = 1 / dtFIL                      # 每秒帧数
    cv.rectangle(frame3, (0,0), (150,40), (0,0,255), -1) # 在左上角画一个实心红色矩形，蓝 绿 红
    cv.putText(frame3, 'fps: '+str(round(fps,1)), (0,30), font, 1, (0,255,255), 2) # 插入帧数文本，保留一位小数,字体1号，黄色，2个字体沉重感

    print("fps = ", fps)

    # cv.imshow('myCam1', frame1)        # 在窗口显示图像1，自适应图像尺寸。
    # cv.imshow('myCam2', frame2)        # 在窗口显示图像2，自适应图像尺寸。
    cv.imshow('comboCam', frame3)        # 显示组合后图像

    # cv.moveWindow('myCam1', 0, 0)      # 窗口坐标，左上角
    # cv.moveWindow('myCam2', 0, 500)    # 窗口坐标，下移500
    cv.moveWindow('comboCam', 0, 0)      # 窗口坐标，左上角

    if cv.waitKey(1) == ord('q'): # 键盘绑定函数
        break
cam.release()
cv.destroyAllWindows() # 破坏创建的所有窗口
