from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval  
import os
from collections import defaultdict
import json
import ujson
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt 
import pylab # matplotlib的一个模块，用于二维、三维图像绘制
pylab.rcParams['figure.figsize'] = (8.0,10.0) # 设置画布大小

dataDir = '/datasets/mscoco/'
dataType = 'train2014' # 以验证集为例
annFile = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
print(annFile)

coco = COCO(annFile)

catIds = coco.getCatIds()
#print("The total number of categories: \n",len(catIds))
#print("Categories Ids: \n",catIds)

cats = coco.loadCats(coco.getCatIds()) # [{'supercategory': 'person', 'id': 1, 'name': 'person'},...]
#print("Categories Names: \n",cats)

nms = [cat['name'] for cat in cats]
print("COCO categories: \n",nms)

sup_nms = set([cat['supercategory'] for cat in cats]) # 使用set()是为了去除重复项
print("COCO supercategories: \n",sup_nms)