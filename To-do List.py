from time import sleep
print('Iniciando sistema...')
sleep(2)
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
        print('-' * 50)
        duvida_tarefa_nova = str(input('-----> Deseja adicionar uma tarefa? s/n:')).strip().upper()[0]
        if duvida_tarefa_nova == 'S':
            quantidade_tarefas = int(input('Quantas tarefas vai querer adicionar?:'))
            for tarefa in range(quantidade_tarefas):
                nova_tarefa = str(input('Nova tarefa:'))
                status_pendente_tarefa.append(nova_tarefa)
            print('--> Todas as {} tarefas foram adicionadas na lista!'.format(quantidade_tarefas))
        elif duvida_tarefa_nova == 'N':
            print('Encerrando programa...')
            sleep(1.2)
        print('-'*50)
    elif opção == 2:
        print('-'*35)
        if status_pendente_tarefa:
            for listagem_pendente in range(len(status_pendente_tarefa)):
                print('Tarefa pendente: {}'.format(status_pendente_tarefa[listagem_pendente]))
        if status_concluída_tarefa:
            for listagem_concluida in range(len(status_concluída_tarefa)):
                print('Tarefa conluída: {}'.format(status_concluída_tarefa[listagem_concluida]))
        print('-'*35)
    elif opção == 3:
        print('-'*45)
        concluir_tarefa = str(input('Deseja concluir alguma tarefa? s/n:')).strip().upper()[0]
        if concluir_tarefa == 'S':
            inspecionar_tarefa = str(input('Digite aqui o nome da tarefa:')).strip()
            if inspecionar_tarefa in status_pendente_tarefa:
                index = status_pendente_tarefa.index(inspecionar_tarefa)
                status_concluída_tarefa.append(status_pendente_tarefa[index])
                status_pendente_tarefa.remove(status_pendente_tarefa[index])
                print('Tarefa marcada como conluída!')
            elif inspecionar_tarefa not in status_pendente_tarefa:
                print('Tarefa não encontrada.')
        elif concluir_tarefa == 'N':
            print('Encerrando programa...')
            sleep(1.2)
        print('-' * 45)
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



