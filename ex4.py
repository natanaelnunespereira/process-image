from skimage import io
import numpy as np
from matplotlib import pyplot as plt

def histograma(img):
    image = io.imread(img)
    
    if image.shape[2] == 3:
        RGB(image)
    else:
        cinza(image)    

def RGB(image):
    dic = {}
    cores = ["azul", "verde", "vermelho"]
    
    for i in range(image.shape[2]):
        dic[i] = {}
        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                if image[x, y, i] in dic[i]:
                    dic[i][image[x, y, i]] += 1
                else:
                    dic[i][image[x, y, i]] = 1
                
        plt.plot(dic[i].values(), color = cores[i])
    
def cinza(image):
    return True

histograma("./imagens/peppers.jpg")