""" 人脸识别 """
import face_recognition
import cv2

print(cv2.__version__)

# 图中有4张人脸
image = face_recognition.load_image_file('/home/jetson/Desktop/jetson-git/demoImages/unknown/u1.jpg')
face_locations = face_recognition.face_locations(image)
print(face_locations)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# 在图上画4个框
for (row1, col1, row2, col2) in face_locations:
# 人脸识别row，col表示行和列，opencv用col, row表示行和列
    cv2.rectangle(image, (col2, row1), (col1, row2), (255,0,0), 2) # 蓝色宽2的框
cv2.imshow('myWindow', image)
cv2.moveWindow('myWindow', 0, 0) 
if cv2.waitKey(0) == ord('q'):
    cv2.destoryAllWindows()   