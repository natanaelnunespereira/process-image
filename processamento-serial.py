#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, os, time, numpy, shutil
from skimage import io

pasta = './images-processamento'
lista_arquivos = glob.glob(pasta + '/*.jpg')
destino = pasta + '/tmp/'

if os.path.exists(destino):
    shutil.rmtree(destino)
    
os.mkdir(destino)

inicio = time.time()

for arquivo in lista_arquivos:
    imagem = io.imread(arquivo)
    altura, largura, profundidade = imagem.shape
    negativo = numpy.zeros((altura, largura, profundidade))
    
    for k in range(profundidade):
        for i in range(altura):
            for j in range(largura):
                negativo[i, j, k] = 255 - imagem[i, j, k]
    
    negativo = negativo.astype(int)
    nome_arquivo = os.path.basename(arquivo)
    io.imsave(destino + nome_arquivo, negativo)    

fim = time.time()
duracao = fim - inicio
minutos, segundos = divmod(duracao, 60)
horas, minutos = divmod(minutos, 60)

print('Tempo decorrido: ' + str(int(horas)).zfill(2) + 'h ' + str(int(minutos)).zfill(2) + 'min ' + str(int(segundos)).zfill(2) + 's')
