#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from skimage import io
import numpy as np
import glob

def main(argv):
    lista = []

    for file in glob.glob('./imagens/subtracao_movimento/*.png'): 
        lista.append(file)
    
    lista = sorted(lista)

    for i in range(len(lista)-1):
        arq = io.imread(lista[i])
        aux = io.imread(lista[i+1])
        aux2 = np.zeros(arq.shape)
        aux2[:,:,3] = 255
        qnt = 0
        qnt2 = 0
        
        for x in range(330, 455):
            for y in range(165, 220):
                qnt += 1
                pixel = arq[x][y].astype(np.int8)
                pixel_aux = aux[x][y].astype(np.int8)
                v = sum(abs(pixel - pixel_aux))
                
                if v >= int(argv[0]):
                    aux2[x][y] = np.array([255, 255, 255, 255], dtype=np.uint8)
                    qnt2 += 1


        if qnt2*100/qnt >= 20:
            io.imsave(f'./imagens/alerta/alerta-{i}.png', aux2)

if __name__ == '__main__':
    main(sys.argv[1:])
