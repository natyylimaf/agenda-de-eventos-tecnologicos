from time import sleep

vetor_dias = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4']
vetor_turnos = ['Manhã', 'Tarde', 'Noite']

matriz_eventos = [
    ['', '', ''], 
    ['', '', ''], 
    ['', '', ''], 
    ['', '', '']
    
    ]


matriz_palestrante = [
    ['', '', ''], 
    ['', '', ''], 
    ['', '', ''], 
    ['', '', '']
    
    ]

# Função para o cadastro de eventos
def cadastro_eventos():
    dias_disponiveis = []  # Cria uma lista vazia para armazenar os índices dos dias que têm pelo menos um turno livre

    # Percorre a matriz de eventos linha por linha, onde cada linha representa um dia
    for i, linha in enumerate(matriz_eventos):
        # Verifica se existe pelo menos um turno vazio nessa linha (dia)
        if '' in linha:
            dias_disponiveis.append(i)  # Se existir, adiciona o índice do dia na lista de dias disponíveis


    # Mostrando os dias disponíveis
    print('===========================================')
    print('\U0001F4C5 Primeiramente, escolha um dia:')
    print('-' * 40)
    print('Dias disponíveis:')

    # Para cada índice de dia disponível, mostra o número (índice) e o nome do dia correspondente em vetor_dias
    for i in dias_disponiveis:
        print(f'{i} - {vetor_dias[i]}')  # # Exemplo: "0 - Dia 1"

    # Loop para garantir que o usuário escolha um dia válido
    while True:
        try:
            linha = int(input('Escolha o número do dia: '))  # Entrada do índice da linha (dia)

            if linha not in dias_disponiveis:
                print('\u274C Dia inválido! Escolha outro.\n')  # Se estiver fora do intervalo, erro
            else:
                break  # Se for válido, sai do loop
        except ValueError:
            print('\u274C Entrada inválida! Digite um número.\n')  # Se digitar texto ou algo não numérico


    # Pegando os turnos do dia escolhido
    turnos_do_dia = matriz_eventos[linha]
    turnos_disponiveis = []  # Lista para armazenar os turnos livres

    # Verificando quais turnos estão vazios
    for j, turno in enumerate(turnos_do_dia):
        if turno == '':
            turnos_disponiveis.append(j)  # Adiciona o índice do turno livre

    # Mostrando os turnos disponíveis
    print('\n\U0001F553 Agora, escolha o turno:')
    print('-' * 40)
    print('Turnos disponíveis:')
    for j in turnos_disponiveis:
        print(f'{j} - {vetor_turnos[j]}')  # Exibe o índice e o nome do turno

    # Loop para garantir uma escolha válida de turno
    while True:
        try:
            coluna = int(input('Escolha o número do turno: '))  # Entrada do índice do turno
        
            if coluna not in turnos_disponiveis:
                print('\u274C Turno inválido! Escolha outro.\n')  # Se não está disponível
            else:
                break  # Turno válido, sai do loop
        except ValueError:
            print('\u274C Entrada inválida! Digite um número.\n')  # Se não digitou um número

        

    # Cadastro do nome do evento e do palestrante
    while True:
        evento = input('\nDigite o nome do evento: ').strip()  # Remove espaços extras
        palestrante = input('Digite o nome do palestrante: ').strip()

        if evento == '' or palestrante == '':
            print('\u2757 Evento ou palestrante não podem ser vazios.')  # Validação para não aceitar campos vazios
        else:
            break  # Dados válidos, sai do loop

    # Armazena os dados nas matrizes correspondentes
    matriz_eventos[linha][coluna] = evento
    matriz_palestrante[linha][coluna] = palestrante

    # Mensagem de sucesso
    print(f'\n\u2705 Evento "{evento}" com palestrante "{palestrante}" cadastrado em {vetor_dias[linha]} no turno {vetor_turnos[coluna]}.\n')
    print('===========================================\n')
    print('\n')



# def listar_eventos():

# def buscar_evento():

# def atualizar_evento():

# def relatorio_por_dia():






def menu():
    while True:
        print('===========================================')
        print('     AGENDA DE EVENTOS TECNOLÓGICOS')
        print('===========================================')
        print('Desenvolvedoras: Micaellen Fagundes e Nathália Lima')
        print('-------------------------------------------')
        print('\u0031\uFE0F\u20E3  - Cadastrar eventos') 
        print('\u0032\uFE0F\u20E3  - Listar eventos')
        print('\u0033\uFE0F\u20E3  - Buscar evento')
        print('\u0034\uFE0F\u20E3  - Atualizar evento')
        print('\u0035\uFE0F\u20E3  - Relatório por dia')
        print('\u0030\uFE0F\u20E3  - Sair')

        opcao = input('Escolha uma opção: ')

        match opcao:

            case '0':
                print('\U0001F6A8 Saindo do programa... Até mais!')
                break
            case '1':
                print('\U0001F195 Opção de cadastro selecionada.\n')
                cadastro_eventos()
            case '2':
                print('\U0001F4DC Opção de listagem selecionada.\n')
                # Chamar a função de listagem de eventos aqui
            case '3':
                print('\U0001F50D Opção de busca selecionada.\n')
                # Chamar a função de buscar eventos aqui
            case '4':
                print('\U0001F4DD Opção de atualização selecionada.\n')
                # Chamar função de atualizar evento aqui
            case '5':
                print('\U0001F4DC Opção de relatório selecionada.\n')
                # Chamar função de relatório aqui

            case _:  # O underline funciona como 'default', ou seja, qualquer valor que não foi capturado nos casos anteriores
                print('\u274C Opção inválida. Tente novamente.\n')
            
        sleep(2)


# Chamando o menu pra iniciar o programa
menu()


