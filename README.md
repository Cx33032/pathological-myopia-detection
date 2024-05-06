# Pathological High Myopia Detection
This project is based on ResNet101 and YOLOv8 to detect the focus that cause high myopia

### <center><a href="#">English</a> | <a href="README_ZH.md">简体中文</a></center>

## Table of Content
[Final Product](#final-product)  
[Dataset Preparation](#dataset-preparation)  
[Quick Start](#quick-start)  
[Reference](#reference)

## Final Product
In the webui, the user can upload an ultra high definition fundus image and type in the name  
  
![input](images/webui_input.png)  
  
The program will run classification model and trained YOLOv8 model to identify the focus (Labeled image and word result)  
  
![output](images/webui_result.png)  
  
After identification, the program will summarize all of the data into a pdf file  
  
![pdf](images/pdf_output.png)  
[Output File](output/Jane_Doe_report.pdf)

## Dataset Preparation
The [dataset](dataset) can be divided into two parts:  
[Classification](#classification)  
[Detection](#detection)  

### Classification
The Classification is mainly classifying the pictures with leopard-spot lesion or not.  

There are two directory under classification:  
```
├─dataset
   ├─classification
      ├─train   <- Training
      │  ├─no       <- Without leopard-spot lesion
      │  └─yes      <- With leopard-spot lesion
      └─val     <- Validation
          ├─no
          └─yes
```

### Detection
Focus list:  
|Name|Label|
|---|---|
|peripapillary atrophy|PPA|
|macular degeneration|MD|
|vitreous opacities|weiss|
|drusen|DR|
|optic disc|OD|
|fuchs dystrophy|Fuch|  
  
#### Peripapillary Atrophy (PPA)
Peripapillary atrophy describes atrophy or thinning in the layers of the retina and retinal pigment epithelium around the optic nerve in the back of the eye  
![PPA](images/PPA_example.png)  

#### Macular Degeneration (MD)  
Age-related macular degeneration is the most common cause of severe loss of eyesight among people 50 and older. Only the center of vision is affected with this disease. It is important to realize that people rarely go blind from it.  
![MD](images/MD_example.png)



## Quick Start
### Install Dependencies
```shell
pip install -r requirements.txt
```
### Train the classification model (Default is ResNet18)
```shell
python classification.py 
```
or use jupyter notebook to run  

### Train YOLOv8 detection model 
```shell
python yolo.py
```
or use jupyter notebook to run

### Run the webui
```shell
Usage: python webui.py [options]

A common command: python webui.py

-l --language       Language of the UI site
```

## Reference
* [【图像分类】实战——使用ResNet实现猫狗分类（pytorch）](https://juejin.cn/post/7012922120392933383)
* [Ultralytics YOLOv8](https://docs.ultralytics.com/modes/train/)
* [搭建一个简单的神经网络LeNet（基于PyTorch）](https://blog.csdn.net/ft_sunshine/article/details/91388812)
* [Gradio Documentation](https://www.gradio.app/docs)
