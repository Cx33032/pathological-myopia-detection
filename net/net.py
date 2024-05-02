import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

# Custom Convolution Neural Network
class CustomCNNReLU(nn.Module):
    def __init__(self):
        super(CustomCNNReLU, self).__init__()
        # Conv2d(input channel size, output channel size, kernel size)
        # Convolution Layer
        self.conv1 = nn.Conv2d(3, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)

        self.fc1 = nn.Linear(14400, 64)
        self.fc2 = nn.Linear(64, 32)
        # Connection with the result
        self.fc3 = nn.Linear(32, 2)
        self.pool = nn.MaxPool2d(2, 2)
    # forward to give the result
    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.conv1(x)) # Activation function: ReLU
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        # flatten the input
        x = x.view(in_size, -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

class CustomCNNSigmoid(nn.Module):
    def __init__(self):
        super(CustomCNNSigmoid, self).__init__()
        
        self.conv1 = nn.Conv2d(3, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)
        
        self.fc1 = nn.Linear(14400, 64)
        self.fc2 = nn.Linear(64, 32)
        
        self.fc3 = nn.Linear(32, 2)
        self.pool = nn.MaxPool2d(2, 2)
    
    def forward(self, x):
        in_size = x.size(0)
        x = F.sigmoid(self.conv1(x)) # Activation function: Sigmoid
        x = self.pool(x)
        x = F.sigmoid(self.conv2(x)) 
        x = self.pool(x)
        
        x = x.view(in_size, -1)
        x = F.sigmoid(self.fc1(x))
        x = F.sigmoid(self.fc2(x))
        x = self.fc3(x)
        return x