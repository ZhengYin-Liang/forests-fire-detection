import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
if __name__ == '__main__':
    model = YOLO('E:/yolov8-20240111/yolov8-main/runs/train/gf resnet50 1003/weights/best.pt')
    model.val(data='E:/yolov8-20240111/yolov8-main/dataset/gf.yaml',
              split='val',
              imgsz=640,
              batch=16,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='GF resnet50',
              )