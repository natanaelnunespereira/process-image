#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from skimage import io
import numpy as np

def main(argv):
    diretorio = argv[0]
    image = io.imread(diretorio)
    
    if len(image.shape) == 3:
        img = RGB(image)   
    else:
        img = cinza(image)

    io.imsave('./imagens/negativo.jpg', img)    

def cinza(image):
    maxValue = np.amax(image)
    image = maxValue - image
    
    return image

def RGB(image):
    image[:,:,0] = np.amax(image[:,:,0]) - image[:,:,0]
    image[:,:,1] = np.amax(image[:,:,1]) - image[:,:,1]
    image[:,:,2] = np.amax(image[:,:,2]) - image[:,:,2]
    
    return image    

if __name__ == '__main__':
    main(sys.argv[1:])