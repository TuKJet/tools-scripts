# 使用方式
增强： python data_aug.py --datapath 'datapath' --aug
还原增强数据：python data_aug.py --datapath 'datapath' --disaug

默认增强的pipline为：
```
transform = A.Compose([
            	A.Rotate(limit=40,p=1),
                A.OneOf([
                	A.RGBShift(p=0.3),
                	A.RandomBrightnessContrast(p=0.3),
            	],p=1),
                A.Flip(p=0.3),
            	A.RandomResizedCrop(image.shape[0],image.shape[1],p=0.3),
                ])
```
其中p为概率

# 数据集目录的结构
--datapath指向分类目录的上一层，比如
    ----train
        ----class1
            --img1
            --img2
            ....
        ----class2
            --img1
            --img2
            ....
        ....
        
在--datapath指向需要增强的train这一级目录。增强后默认存在对应分类的文件夹下，命名规则为：  aug(单张图增强次数)_{32位乱码}.jpg

# 参数：
--datapath  数据集路径
--augnum  单张图像数据增强次数
--aug  增强数据开关
--disaug  还原增强数据开关