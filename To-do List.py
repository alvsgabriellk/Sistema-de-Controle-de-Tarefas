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



