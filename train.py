import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
if __name__ == '__main__':
    model = YOLO('E:/yolov8-20240111/yolov8-main/ultralytics/cfg/models/v8/resnet50.yaml')
    model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='E:/yolov8-20240111/yolov8-main/dataset/gf.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=4,
                close_mosaic=10,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='runs/train',
                name='gf resnet50new 100',
                )