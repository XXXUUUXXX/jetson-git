import cv2 as cv

print(cv.__version__)

width = 800  # 800 640 1280 1920
height = 600 # 600 480 720  1080
flip=2

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
camSet = 'nvarguscamerasrc sensor-id=0 ee-mode=2 ee-strength=0 tnr-mode=3 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=‘+str(flip)+’ ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.15 saturation=1.2 ! appsink' 
cam = cv.VideoCapture(camSet)

# USB摄像头捕获
# 方法一
# cam = cv.VideoCapture('/dev/video0') 
# 方法二，没成功运行
# camSet = 'v4l2src device=/dev/video0 ! video/x-raw, width='+str(width)+', height='+str(height)+', framerate=25/1 ! videoconvert ! appsink'
# cam = cv.VideoCapture(camSet)

while True:
    _, frame = cam.read()
    cv.moveWindow('myCam', 0, 0)  # 窗口坐标，左上角
    cv.imshow('myCam', frame)     # 在窗口显示图像，自适应图像尺寸。
    if cv.waitKey(1) == ord('q'): # 键盘绑定函数
        break
cam.release()
cv.destroyAllWindows() # 破坏创建的所有窗口
