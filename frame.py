#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:15:28 2022

@author: drabaz
"""

import sys
from skimage import io
import numpy as np
import glob
from natsort import natsorted

lista = []
for file in glob.glob('/media/drabaz/BACKUP/SISTEMAS DE INFORMAÇÃO/8º PERÍODO/Tópicos Especiais em Linguagens de Programação/Exercicio/Final/imagens/subtracao_movimento/*.png'): 
    lista.append(file)
 
lista.sort()
#print(lista)
print(io.imread(lista[0][]))
for i in lista:
    #arq = io.imread(lista.i)
    #arq2 = io.imread(lista.i+1)
