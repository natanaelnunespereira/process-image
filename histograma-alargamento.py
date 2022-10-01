from skimage import io
import numpy as np
from matplotlib import pyplot as plt

def histograma(img):
    image = io.imread(img)
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

def alargamento(img, a, b):
    image = io.imread(img)
    image_alarg = image*a+b    
    io.imsave('./imagens/alargamento.jpg', image_alarg)
    io.imshow(image_alarg)
    
#histograma("./imagens/peppers.jpg")
alargamento("./imagens/peppers.jpg", 0.5, 2)