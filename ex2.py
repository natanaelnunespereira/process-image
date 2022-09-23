from skimage import io
import numpy as np

image = io.imread('./imagens/peppers.jpg')
maxValue = np.amax(image)
blue_channel = image[:,:,0]
negativeImage = maxValue - blue_channel
io.imsave('./imagens/peppers_negativo.jpg', negativeImage)
io.imshow(negativeImage) 