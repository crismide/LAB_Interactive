import torch
from torch.utils.data import Dataset
import pandas as pd
import numpy
from torch import nn

class MyNeuralNetwork(nn.Module):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.net = nn.Sequential(
            nn.Linear(22, 100)
            nn.ReLU()
            nn.Linear(100, 3) 
        )
    
    def forward(self,input):
        return self.net()
        

class MultiEmoVA(Dataset):
    def __init__(self, data_path):
        super().__init__()


def main():
    data = MultiEmoVA("Face-Feat.txt")
    print(data[15])

if __name__ == "main":
    main()