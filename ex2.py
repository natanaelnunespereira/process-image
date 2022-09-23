from skimage import io
import numpy as np

image = io.imread('./imagens/peppers.jpg')
image[:,:,0] = np.amax(image[:,:,0]) - image[:,:,0]
image[:,:,1] = np.amax(image[:,:,1]) - image[:,:,1]
image[:,:,2] = np.amax(image[:,:,2]) - image[:,:,2]
io.imsave('./imagens/peppers_negativo.jpg', image)
io.imshow(image) 