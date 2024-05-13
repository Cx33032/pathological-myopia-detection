# Pathological High Myopia Detection
This project is based on ResNet101 and YOLOv8 to detect the focus that cause high myopia

## <div align="center"><b><a href="README.md">English</a> | <a href="README_ZH.md">简体中文</a></b></div>

## Ackowledgement
#### I do not have much specialize knowledge on ophthalmology and I am doing this because this is a meaningful project to learn and deploy. If there is any problems related to my contents, welcome to pull request or post and issue. Thanks a lot! 

## Table of Content
- [Final Product](#final-product)  
- [Dataset Preparation](#dataset-preparation)  
- [Quick Start](#quick-start)  
- [Reference](#reference)
- [Acknowledgement](#ackowledgement)

## Final Product
In the webui, the user can upload an ultra high definition fundus image and type in the name  
  
![input](images/webui_input.png)  
  
The program will run classification model and trained YOLOv8 model to identify the focus (Labeled image and word result)  
  
![output](images/webui_result.png)  
  
After identification, the program will summarize all of the data into a pdf file  
  
![pdf](images/pdf_output.png)  
[Output File](output/Jane_Doe_report.pdf)

## Dataset Preparation
#### The [dataset](dataset) can be divided into two parts:  
- [Classification](#classification)  
- [Detection](#detection)  

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

#### Vitreous Opacities (weiss)
Vitreous opacities are floating objects inside the vitreous body. They can be of different sizes, shapes and densities. New objects are treated conservatively, and laser treatment is not usually indicated until the floaters stabilize in size and density.  
  
![weiss](images/weiss_example.png)  

#### Drusen (DR)
Drusen bodies are extracellular deposits of lipids, proteins, and cellular debris which are found within the layers of the retina and appear as small, yellow deposits on dilated eye exams.  
  
![DR](images/drusen_example.jpg)  

#### Optic Disc (OD)
The optic disc is the round spot on the retina formed by the passage of the axons of the retinal ganglion cells, which transfer signals from the photoreceptors of the eye to the optic nerve, allowing us to see.  
  
![OD](images/normal_example.png)  

#### Fuchs Dystrophy (Fuchs)
Fuchs (pronounced "fooks") dystrophy is an eye disease in which cells lining the inner surface of the cornea slowly start to die off. The disease most often affects both eyes.  

## Quick Start
### Install Dependencies
Installastion of PyTorch: [link](https://pytorch.org/)  

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
