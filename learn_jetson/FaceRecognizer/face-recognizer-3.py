""" 人脸识别 """
import face_recognition
import cv2 as cv
import os
import pickle


print(cv.__version__)

Encodings = []
Names = []
image_dir = '/home/jetson/Desktop/jetson-git/demoImages/known'
# os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
for root,dirs,files in os.walk(image_dir):
    for file in files:
        fullPath = os.path.join(root, file)
        print(fullPath)
        # 从后往前搜索.分割后缀名
        name = os.path.splitext(file)[0]
        print(name)
        person = face_recognition.load_image_file(fullPath)
        encoding = face_recognition.face_encodings(person)
        Encodings.append(encoding)
        Names.append(name)
    print(Names)
    # 备份
    with open('train.pkl', "wb") as f:
        pickle.dump(Names, f)
        pickle.dump(Encodings, f)
