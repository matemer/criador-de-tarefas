def criar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
        
criar_arquivo('teste.txt', 'este arquivo e um teste')