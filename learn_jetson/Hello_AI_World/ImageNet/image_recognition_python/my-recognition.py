"""
图像识别python版本
"""
#! /usr/bin/python3

import jetson.inference # 识别图像
import jetson.utils     # 加载图像
import argparse

# 解析命令行
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be: googlenet, resnet-18, ect.")
opt = parser.parse_args()

# 加载图片到cpu/gpu内存
img = jetson.utils.loadImage(opt.filename)

# 加载识别网络
net = jetson.inference.imageNet(opt.network)

# 分类图像
class_idx, confidence = net.Classify(img)

# 找到目标表述
class_desc = net.GetClassDesc(class_idx)

# 打印结果
print("image is recognized as '{:s}' (class ${:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))