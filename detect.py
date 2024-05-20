import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('E:/yolov8-20240111/yolov8-main/runs/train/yolov6/weights/best.pt') # select your model.pt path
    model.predict(source='C:/Users/Administrator/Desktop/yuan',
                  imgsz=640,
                  project='runs/detect',
                  name='yolov6-v-yuan',
                  save=True,
                #   visualize=True # visualize model features maps
                )