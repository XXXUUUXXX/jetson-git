"""
使用命令： python3 my-detection.py 运行
"""

import jetson.inference
import jetson.utils

# model有：
# ssd-mobilenet-v1
# ssd-mobilenet-v2
# ssd-inception-v2
# coco-dog
# coco-bottle
# coco-chair
# coco-airplane
# pednet
# multiped
# facenet
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img)
    print(detections)
    display.Render(img)
    display.SetStatus("object detection | network {:.0f} FPS".format(net.GetNetworkFPS()))
