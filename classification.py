# -*-   Coding with utf-8   -*- #
# -*- Developed by Harryjin -*- #

import torch.optim as optim
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models
from torch.autograd import Variable
import matplotlib.pyplot as plt
import pandas as pd
from net import *
from tqdm import tqdm

# Basic Traning Settings
BATCH_SIZE = 64
EPOCHS = 30
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(DEVICE)

# Data transformation
transform = transforms.Compose([      
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])

])
transform_test = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

# Read Data
dataset_train = datasets.ImageFolder('./dataset/classification/train', transform)
print(dataset_train.imgs)
# Read the label
print(dataset_train.class_to_idx)
dataset_test = datasets.ImageFolder('./dataset/classification/val', transform_test)
# Read the label
# print(dataset_test.class_to_idx)

# Load the data using DataLoader
train_loader = torch.utils.data.DataLoader(dataset_train, batch_size=BATCH_SIZE, shuffle=True, drop_last=True, num_workers = 1)
test_loader = torch.utils.data.DataLoader(dataset_test, batch_size=BATCH_SIZE, shuffle=False, drop_last=True, num_workers = 1)
modellr = 1e-4

# Resnet18 Example

# Instantiate the model
criterion = nn.CrossEntropyLoss() # Loss function

model = torchvision.models.resnet18(pretrained=True) # Use ResNet18
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.to(DEVICE)
# Using the most powerful optimizer - Adam
optimizer = optim.Adam(model.parameters(), lr=modellr)

df_train = pd.DataFrame(columns = ['epoch', 'train_loss', 'val_loss', 'accuracy'])

def adjust_learning_rate(optimizer, epoch):
    """Sets the learning rate to the initial LR decayed by 10 every 20 epochs"""
    modellrnew = modellr * (0.1 ** (epoch // 20))
    # print("lr:", modellrnew)
    for param_group in optimizer.param_groups:
        param_group['lr'] = modellrnew


# Train method

def train(model, device, train_loader, optimizer, epoch):
    model.train()
    sum_loss = 0
    total_num = len(train_loader.dataset)

    loop = tqdm(enumerate(train_loader), total = len(train_loader)) # Showing progress bar with tqdm
    for batch_idx, (data, target) in loop:
        data, target = Variable(data).to(device), Variable(target).to(device)
        output = model(data)

        loss = criterion(output, target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print_loss = loss.data.item()
        sum_loss += print_loss
        loop.set_description(f'Epoch [{epoch}/{EPOCHS}]')
        loop.set_postfix_str('loss = {:6f}'.format(loss.item()))
    ave_loss = sum_loss / len(train_loader)
    
    torch.save(model, './checkpoints/model_{}.pth'.format(epoch)) # Save every epoch
    return ave_loss 

# Validate the model every epoch
def val(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    total_num = len(test_loader.dataset)
    
    with torch.no_grad():
        for data, target in test_loader:
            data, target = Variable(data).to(device), Variable(target).to(device)
            output = model(data)
            loss = criterion(output, target)
            _, pred = torch.max(output.data, 1)
            correct += torch.sum(pred == target)
            print_loss = loss.data.item()
            test_loss += print_loss
        correct = correct.data.item()
        acc = correct / total_num
        avgloss = test_loss / len(test_loader)
        print('Val set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            avgloss, correct, len(test_loader.dataset), 100 * acc))
        return acc, avgloss

def main():
    # Train
    for epoch in range(1, EPOCHS + 1):
        adjust_learning_rate(optimizer, epoch)
        loss = train(model, DEVICE, train_loader, optimizer, epoch)
        acc, aveloss = val(model, DEVICE, test_loader)
        df_train.loc[len(df_train.index)] = [epoch, loss, aveloss, acc] # Save the traning and validation data every epoch to a csv
    torch.save(model, 'model.pth') # Save the model
    df_train.to_csv('loss.csv')

    # Show the traning result with matplotlib
    df = pd.read_csv('./loss.csv')
    df[['train_loss', 'val_loss', 'accuracy']].plot()

    plt.show()

if __name__ == '__main__':
    main()