import os

def renomear_arquivos(diretorio,padrao):
    for arquivo in os.listdir(diretorio):
        nome_atual = os.path.join(diretorio, arquivo)
        novo_nome = os.path.join(diretorio, padrao % arquivo[0:-4])
        os.rename(nome_atual, novo_nome)
        
renomear_arquivos("/home/nunetan/Documentos/enutilidades/", "arquivo_%s.txt") 
