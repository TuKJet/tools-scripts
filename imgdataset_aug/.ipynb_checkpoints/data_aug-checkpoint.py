# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:19:58 2021

@author: DELL
"""
import albumentations as A
import cv2
import sys
import os
import re
import shutil
import string
import random
import argparse

def check_dataset(root_path):#check dataset is already augmented
    for i in os.listdir(root_path):
        for j in os.listdir(f'{root_path}/{i}'):
            if re.match('^aug\d+_.{32}\.jpg$', j):
                print(f'{root_path}/{i}/{j}')
                return False
    return True

def deletedataset_augimage(root_path):
    for i in os.listdir(root_path):
        for j in os.listdir(f'{root_path}/{i}'):
            if re.match('^aug\d+_.{32}\.jpg$', j):
                os.remove(f'{root_path}/{i}/{j}')
    return True

def augment_dataset(args):         
    for i in os.listdir(args.datapath):
        for j in os.listdir(f'{args.datapath}/{i}'):
            image = cv2.imread(f'{args.datapath}/{i}/{j}')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            for x in range(args.augnum):
                transform = A.Compose([
            	A.Rotate(limit=40,p=1),
                A.OneOf([
                	A.RGBShift(p=0.3),
                	A.RandomBrightnessContrast(p=0.3),
            	],p=1),
                A.Flip(p=0.3),
            	A.RandomResizedCrop(image.shape[0],image.shape[1],p=0.3),
                ])
                
                transformed = transform(image=image)
                transformed_image = transformed["image"]
                
                save_name = f'aug{x}_'+''.join(random.sample(string.ascii_letters + string.digits, 32))+'.jpg'
                cv2.imwrite(os.path.join(f'{args.datapath}/{i}/'+save_name),transformed_image)
   
def main(args):
    if args.aug:
        if check_dataset(args.datapath):
            augment_dataset(args)
        else:
            print("image dataset has been auged!!!!  disaug dataset first!!")
            return False
            
    if args.disaug:
        deletedataset_augimage(args.datapath)
            
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", help="train path of dataset ", type=str, default="")
    parser.add_argument("--augnum", help="num of image aug times ", type=int, default=5)
    parser.add_argument('--aug', action='store_true', default=False,help='aug the dataset')
    parser.add_argument('--disaug', action='store_true', default=False,help='disaug the dataset')
    args = parser.parse_args()
    main(args)