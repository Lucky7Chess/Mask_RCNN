import os
from PIL import Image
import skimage.draw
import skimage.io
import numpy as np
import sys
pathLabels =  "../../datasets/lanedetect/train/labels/Record001/Camera 5"
pathRaw = "../../datasets/lanedetect/train/raw/Record001/Camera 5"
for root, dirs, files in os.walk(pathRaw):
    for filename in files:
        print(filename)
        print(filename[:-4] + str("_bin.png"))
        pathTo = pathLabels + "/" +  filename[:-4] + str("_bin.png")
        print(pathTo)
        image = skimage.io.imread(pathTo)
        print(image.shape)
        print(image[:,:,3] > 0)
        np.set_printoptions(threshold=sys.maxsize)
        #print(image[:,:,2] > 0)
        im = Image.open(os.path.join(pathRaw, filename))
        print(im.size)
