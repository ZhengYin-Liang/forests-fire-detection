# project brief

This project designed a fire and smoke detection model, FireYOLO-Lite. This project is mainly a development document for this task. The data set used in this experiment is M4SFWD (reference)[M4SFWD: A Multi-Faceted synthetic dataset for remote sensing forest wildfires detection - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417424003543)），The backbone network of its model is replaced by GhostNetV2, and a multi-scale and wide-field attention mechanism CPDCA is integrated. Neck follows the design method of YOLOv8, highlighting lightweight design ideas.
![image1](https://github.com/ZhengYin-Liang/forests-fire-detection/blob/master/dataset/Figure3.jpg?raw=true)
# tutorial

1.Training models to use files`/train.py`
2.Verify model usage files`/val.py`
3.Test model use file`/test_yaml.py`
4.Test model FPS using files`/get_FPS.py`，Modify the parameters in `parser.add_argument`
5.Data set path modification`/datasets/fire.yaml`
# Results show
FireYOLO-Lite is compared with YOLOv3-tiny, MobileNetV3, and ShuffleNetV2, all lightweight models, in dataset M4SFWD.
![image2](https://github.com/ZhengYin-Liang/forests-fire-detection/blob/master/dataset/Figure9.jpg?raw=true)
