""" 人脸识别 """
""" 对已知人脸进行训练 """
import face_recognition
import cv2
import pickle

print(cv2.__version__)

# 加载
with open('train.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

# 字体
font = cv2.FONT_HERSHEY_SIMPLEX

# 测试未知图像
testImage = face_recognition.load_image_file('/home/jetson/Desktop/jetson-git/demoImages/unknown/u4.jpg')
facePositions = face_recognition.face_locations(testImage)
allEncodings = face_recognition.face_encodings(testImage, facePositions)
testImage = cv2.cvtColor(testImage, cv2.COLOR_RGB2BGR)
# for遍历 --- zip（）
for (top, right, bottom, left), face_encoding in zip(facePositions, allEncodings):
    name = 'Unknown'
    matches = face_recognition.compare_faces(Encodings, face_encoding)
    print(matches)
    if True in matches:
        first_match_index = matches.index(True)
        name = Names[first_match_index]
    cv2.rectangle(testImage, (left,top), (right,bottom), (255,0,0), 2)
    # 加标签
    cv2.rectangle(testImage, (left,top), (left+200, top+30), (0,255,255), -1)
    cv2.putText(testImage, name, (left,top+20), font, .75, (255,0,0), 2)
cv2.imshow('myWindow', testImage)
cv2.moveWindow('myWindow', 0, 0)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyALLWindows()
