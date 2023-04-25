import os
from shutil import move

def mover_arquivos(origem, destino):
    for arquivo in os.listdir(origem):
        if arquivo.endswith('.txt'):
            move(origem + arquivo, destino + 'Documentos/')
        elif arquivo.endswith('.jpg'):
            move(origem + arquivo, destino + 'Imagens/')
        elif arquivo.endswith('.pdf'):
            move(origem + arquivo, destino + 'Documentos/')
            
mover_arquivos('/home/nunetan/Documentos/codigos_especiais/', '/home/nunetan/')