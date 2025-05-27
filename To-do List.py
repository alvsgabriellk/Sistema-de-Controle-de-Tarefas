from time import sleep
print('Iniciando sistema...')
sleep(2)
lista_tarefas_novas = []
status_pendente_tarefa = []
status_concluída_tarefa = []
print('-='*20)
print('   ------------MENU ABERTO------------')
print('''    [ 1 ] | Adicionar tarefas
    [ 2 ] | Listar todas as tarefas
    [ 3 ] | Marcar tarefas como concluídas
    [ 4 ] | Remover tarefas
    [ 5 ] | Filtrar tarefas
    [ 6 ] | Sair do sistema''')
print('-='*20)
opção = int(input('-----> Digite aqui a alternativa:'))
while opção != 6:
    if opção == 1:
        duvida_tarefa_nova = str(input('-----> Deseja adicionar uma tarefa? s/n:')).strip().upper()[0]
        if duvida_tarefa_nova == 'S':
            quantidade_tarefas = int(input('Quantas tarefas vai querer adicionar?:'))
            for tarefa in range(quantidade_tarefas):
                nova_tarefa = str(input('Nova tarefa:'))
                lista_tarefas_novas.append(nova_tarefa)
                status_pendente_tarefa.append(nova_tarefa)
            print('--> Todas as {} tarefas adicionadas na lista!.'.format(quantidade_tarefas))
        elif duvida_tarefa_nova == 'N':
            print('Encerrando programa...')
            sleep(1.2)
        print('-'*50)
    print('-=' * 20)
    print('   ------------MENU ABERTO------------')
    print('''    [ 1 ] | Adicionar tarefas
    [ 2 ] | Listar todas as tarefas
    [ 3 ] | Marcar tarefas como concluídas
    [ 4 ] | Remover tarefas
    [ 5 ] | Filtrar tarefas
    [ 6 ] | Sair do sistema''')
    print('-=' * 20)
    opção = int(input('-----> Digite aqui a alternativa:'))



