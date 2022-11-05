#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, os, time, numpy, multiprocessing, shutil
from skimage import io

def processar_imagens(camimho_arquivo, destino_arquivo):
    imagem = io.imread(camimho_arquivo)
    altura, largura, profundidade = imagem.shape
    negativo = numpy.zeros((altura, largura, profundidade))
    
    for k in range(profundidade):
        for i in range(altura):
            for j in range(largura):
                negativo[i, j, k] = 255 - imagem[i, j, k]
    
    negativo = negativo.astype(int)
    nome_arquivo = os.path.basename(camimho_arquivo)
    io.imsave(destino_arquivo + nome_arquivo, negativo) 

pasta = './images-processamento'
lista_arquivos = glob.glob(pasta + '/*.jpg')
destino = pasta + '/tmp/'

if os.path.exists(destino):
    shutil.rmtree(destino)
    
os.mkdir(destino)

inicio = time.time()

for arquivo in lista_arquivos:
    processo = multiprocessing.Process(target=processar_imagens, args=(arquivo, destino))
    processo.start()
    #processar_imagens(arquivo, destino)       

fim = time.time()
duracao = fim - inicio
minutos, segundos = divmod(duracao, 60)
horas, minutos = divmod(minutos, 60)

print('Tempo decorrido: ' + str(int(horas)).zfill(2) + 'h ' + str(int(minutos)).zfill(2) + 'min ' + str(int(segundos)).zfill(2) + 's')
