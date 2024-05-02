# -*-   Coding with utf-8   -*- #
# -*- Developed by Harryjin -*- #

from ultralytics import YOLO

model = YOLO(r'./pretrained/yolov8s.pt')
result = model.train(data = r'./dataset/2/myotia.yaml', epochs = 300, batch = 32)