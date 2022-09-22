from skimage import io
import numpy as np

image = io.imread('./imagens/peppers.jpg')
maxValue = np.amax(image)
negativeImage = maxValue - image
io.imsave('./imagens/mpeppers_negativo.jpg', negativeImage)
io.imshow(negativeImage)
           