from skimage import io
import numpy as np

image = io.imread('/imagens/mamografia.jpg')
maxValue = np.amax(image)
negativeImage = maxValue - image
io.imsave('/imagens/mamografia_negativo.jpg', negativeImage)
io.imshow(negativeImage)