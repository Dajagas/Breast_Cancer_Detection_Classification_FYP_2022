import pandas as pd
import numpy as np
from PIL import Image
import os
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mias_dataset_path', type=str, required=True)
parser.add_argument('--mias_dump_path', type=str, required=True)
class Converter:
    
    def pgm2png(self,dataset_path,dump_path):
        
        for file in tqdm(os.listdir(dataset_path)):
            filename, extension  = os.path.splitext(file)
            if extension == ".pgm":
                new_file = "{}.png".format(filename)
                file = dataset_path + "\\"+file
                with Image.open(file) as im:
                    im.save(dump_path+"\\"+new_file)

if __name__ == "__main__":
    converter_object = Converter()
    args = parser.parse_args()
    dataset_path = args.mias_dataset_path
    dump_path = args.mias_dump_path
    
    converter_object.pgm2png(dataset_path,dump_path)
    print("All files converted")