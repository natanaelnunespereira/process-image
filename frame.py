import sys
from skimage import io
import numpy as np
import glob
from natsort import natsorted

lista = []
for file in glob.glob('./imagens/subtracao_movimento/*.png'): 
    lista.append(file)
 
lista.sort()
#print(lista)
print(io.imread(lista[0][]))
for i in lista:
    #arq = io.imread(lista.i)
    #arq2 = io.imread(lista.i+1)
