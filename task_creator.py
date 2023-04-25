lista = []

#Criação da def
def add_tarefa():
    #Criando o contador
    contador = 0
    #Loop que realiza a pergunta até o contador chegar em 10
    while contador < 10:
        #Pedido de dado para o usuário final
        tarefa = input("Adicione uma tarefa: ")
        #Condicional if que verifica se o valor esta incluso na lista
        if tarefa not in lista:
            #Adiciona +1 ao contador
            contador += 1
            #Informa que o usuário final quer adicionar
            print("Você quer adicionar")
            #Adicionando valor na lista
            lista.append(tarefa)
            #Informando que o valor foi adicionado na lista
            print(f'{tarefa} foi adicionado a lista e é o {contador}º valor')
        #Se o valor já esta na lista ele será deletado
        else:
            #Valor retirado do contadaor pois será deletado
            contador -= 1
            #Removendo da lista
            lista.remove(tarefa)
            #Informando o usuário final que o valor inserido foi deletado
            print(f"O valor '{tarefa}' foi deletado")

    #Formatando a lista que será apresentada
    for indice, valor in enumerate(lista):
        #Formatação da lista apresentada ao usuário final
        lista_enumerada = str(indice + 1) + ' - ' + str(valor)
        #Enviando a lista formatada para o usuário final
        print(f'As tarefas de hoje são: {lista_enumerada}')

add_tarefa()