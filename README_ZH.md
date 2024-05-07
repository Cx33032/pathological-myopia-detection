# 病理性高度近视检测
基于ResNet和YOLOv8的病理性高度近视检测

## <div align="center"><b><a href="README.md">English</a> | <a href="README_ZH.md">简体中文</a></b></div>

## 目录
- [成果](#成果)  
- [数据集准备](#数据集准备)  
- [快速开始](#快速开始)  
- [参考](#参考)

## 成果
在最后的webui中，使用者可以输入患者名称并上传患者的超高清眼底图彩照  
  
![input](images/webui_input.png)  
  
模型会首先进行分类（是否有豹纹状改变）然后会用YOLOv8来识别病灶  
  
![output](images/webui_result.png)  
  
识别完成后，会总结所有的结果并同时输出到webui和pdf文件中  
  
![pdf](images/pdf_output.png)  
#### [输出文件](output/Jane_Doe_report.pdf)

## 数据集准备
[数据集](dataset)分为两部分:  
[分类](#分类)  
[检测](#检测)  

### 分类
分类算法会对患者的眼底图进行分类：有无豹纹状改变  

在[dataset/classification](dataset/classification)文件夹下有两个子文件夹:  
```
├─dataset
   ├─classification
      ├─train   <- 训练集
      │  ├─no       <- 没有豹纹状改变
      │  └─yes      <- 有豹纹状改变
      └─val     <- 测试集
          ├─no
          └─yes
```

### 检测
病灶类型:  
|英文名|中文名|标签|
|---|---|---|
|peripapillary atrophy|视盘萎缩斑|PPA|
|macular degeneration|黄斑萎缩|MD|
|vitreous opacities|玻璃体浑浊|weiss|
|drusen|玻璃膜疣|DR|
|optic disc|正常视盘|OD|
|fuchs dystrophy|福斯氏角膜内皮营养不良|Fuchs|  
  
#### Peripapillary Atrophy 视盘萎缩斑 (PPA)
Peripapillary atrophy describes atrophy or thinning in the layers of the retina and retinal pigment epithelium around the optic nerve in the back of the eye  
![PPA](images/PPA_example.png)  

#### Macular Degeneration 黄斑萎缩 (MD)  
Age-related macular degeneration is the most common cause of severe loss of eyesight among people 50 and older. Only the center of vision is affected with this disease. It is important to realize that people rarely go blind from it.  
![MD](images/MD_example.png)

#### Vitreous Opacities 玻璃体浑浊 (weiss)
Vitreous opacities are floating objects inside the vitreous body. They can be of different sizes, shapes and densities. New objects are treated conservatively, and laser treatment is not usually indicated until the floaters stabilize in size and density.  
![weiss](images/weiss_example.png)  

#### Drusen 玻璃膜疣 (DR)
Drusen bodies are extracellular deposits of lipids, proteins, and cellular debris which are found within the layers of the retina and appear as small, yellow deposits on dilated eye exams.  
![DR](images/drusen_example.jpg)  

#### Optic Disc 正常视盘 (OD)
The optic disc is the round spot on the retina formed by the passage of the axons of the retinal ganglion cells, which transfer signals from the photoreceptors of the eye to the optic nerve, allowing us to see.  
![OD](images/normal_example.png)  

#### Fuchs Dystrophy 福斯氏角膜内皮营养不良 (Fuchs)
Fuchs (pronounced "fooks") dystrophy is an eye disease in which cells lining the inner surface of the cornea slowly start to die off. The disease most often affects both eyes.  

## 快速开始
### 下载依赖
```shell
pip install -r requirements.txt
```
### 训练分类算法（网络结构默认ResNet18）
```shell
python classification.py 
```
或者使用jupyter notebook  

### 训练YOLOv8
```shell
python yolo.py
```
或者使用jupyter notebook  

### 运行webui
```shell
Usage: python webui.py [options]

A common command: python webui.py

-l --language       Language of the UI site
```

## 参考
* [【图像分类】实战——使用ResNet实现猫狗分类（pytorch）](https://juejin.cn/post/7012922120392933383)
* [Ultralytics YOLOv8](https://docs.ultralytics.com/modes/train/)
* [搭建一个简单的神经网络LeNet（基于PyTorch）](https://blog.csdn.net/ft_sunshine/article/details/91388812)
* [Gradio Documentation](https://www.gradio.app/docs)