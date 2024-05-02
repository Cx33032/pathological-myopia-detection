# pathological-myopia-detection
This project is based on ResNet101 and YOLOv8 to detect the focus that cause high myopia

## Table of Content
[Final Product](#final-product)  
[Preparation](#preparation)  
[Run](#run)  

## Final Product

## Preparation

## Run
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