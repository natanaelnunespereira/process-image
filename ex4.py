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
    
    return True
    
def cinza(image):
    fig, ax = plt.subplots()
    plt.imshow(image, cmap="gray")
    plt.figure()
    plt.title("Cinza")
    plt.xlabel("Cinza")
    plt.ylabel("Quantidade de pixel")
    plt.xlim([0.0, 1.0])
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    plt.plot(bin_edges[0:-1], histogram)

histograma("./imagens/peppers.jpg")