import sys
from skimage import io
import numpy as np

def main(argv):
    diretorio = argv[0]
    image = io.imread(diretorio)
    
    if image.shape[2] == 1:
        cinza(diretorio)
    elif image.shape[2] == 3:
        RGB(diretorio)
        

if __name__ == '__main__':
    main(sys.argv[1:])

def cinza(img):
    image = io.imread(img)
    maxValue = np.amax(image)
    negativeImage = maxValue - image
    io.imsave(img, negativeImage)

def RGB(img):
    image = io.imread(img)
    image[:,:,0] = np.amax(image[:,:,0]) - image[:,:,0]
    image[:,:,1] = np.amax(image[:,:,1]) - image[:,:,1]
    image[:,:,2] = np.amax(image[:,:,2]) - image[:,:,2]
    io.imsave(img, image)