#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
from skimage import io
import numpy as np
from matplotlib import pyplot as plt

def main(argv):
    getopt.getopt(argv, ["dic", "a", "b"])
    image = io.imread(argv[0])

    if len(image.shape) == 3:
        img = RGB(image)   
    else:
        img = cinza(image)

    io.imsave('./imagens/negativo.jpg', img)    
    histograma(image)
    alargamento(argv[0], float(argv[1]), float(argv[2]))

def cinza(image):
    maxValue = np.amax(image)
    image_aux = maxValue - image
    
    return image_aux

def RGB(image):
    image[:,:,0] = np.amax(image[:,:,0]) - image[:,:,0]
    image[:,:,1] = np.amax(image[:,:,1]) - image[:,:,1]
    image[:,:,2] = np.amax(image[:,:,2]) - image[:,:,2]
    
    return image

def histograma(image):
    dic = {}
    cores = ["blue", "green", "red"]
    
    if len(image.shape) < 3:
        image = image[:, :, np.newaxis]
    
    for i in range(image.shape[2]):
        dic[i] = {}
        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                if image[x, y, i] in dic[i]:
                    dic[i][image[x, y, i]] += 1
                else:
                    dic[i][image[x, y, i]] = 1
                
        plt.plot(list(dic[i].values()), color = cores[i])
    
    plt.show()

def alargamento(image, a, b):
    image = io.imread(image)
    image = image*a+b    
    io.imsave('./imagens/alargamento.jpg', image)

if __name__ == '__main__':
    main(sys.argv[1:])