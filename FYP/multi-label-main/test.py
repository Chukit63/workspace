import os
from pycocotools.coco import COCO
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

json_path = '/datasets/mscoco/annotations/instances_val2014.json'
img_path = "/datasets/mscoco/val2017"

json_labels = json.load(open(json_path, "r"))
print(json_labels['info'])  