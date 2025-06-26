from time import sleep

vetor_dias = ['Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
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


def cadastro_eventos():
    dias_disponiveis = [] 

    for i, linha in enumerate(matriz_eventos):
        if '' in linha:
            dias_disponiveis.append(i)


    print('===========================================')
    print('\U0001F4C5 Primeiramente, escolha um dia:')
    print('-' * 40)
    print('Dias disponíveis:')

    for i in dias_disponiveis:
        print(f'{i} - {vetor_dias[i]}')

    while True:
        try:
            linha = int(input('Escolha o número do dia: ')) 

            if linha not in dias_disponiveis:
                print('\u274C Dia inválido! Escolha outro.\n') 
            else:
                break  
        except ValueError:
            print('\u274C Entrada inválida! Digite um número.\n') 


    turnos_do_dia = matriz_eventos[linha]
    turnos_disponiveis = []  

    for j, turno in enumerate(turnos_do_dia):
        if turno == '':
            turnos_disponiveis.append(j)  

    print('\n\U0001F553 Agora, escolha o turno:')
    print('-' * 40)
    print('Turnos disponíveis:')
    for j in turnos_disponiveis:
        print(f'{j} - {vetor_turnos[j]}')  

    while True:
        try:
            coluna = int(input('Escolha o número do turno: '))  
        
            if coluna not in turnos_disponiveis:
                print('\u274C Turno inválido! Escolha outro.\n')  
            else:
                break  
        except ValueError:
            print('\u274C Entrada inválida! Digite um número.\n')  
 
    while True:
        evento = input('\nDigite o nome do evento: ').strip()  
        palestrante = input('Digite o nome do palestrante: ').strip()

        if evento == '' or palestrante == '':
            print('\u2757 Evento ou palestrante não podem ser vazios.') 
        else:
            break  

    matriz_eventos[linha][coluna] = evento
    matriz_palestrante[linha][coluna] = palestrante

    print(f'\n\u2705 Evento "{evento}" com palestrante "{palestrante}" cadastrado em {vetor_dias[linha]} no turno {vetor_turnos[coluna]}.\n')
    print('===========================================\n')
    print('\n')


def listar_eventos():
    print('===========================================')

    for i in range(len(vetor_dias)): 
        print(f'\U0001F4C5 {vetor_dias[i]}:')
        
        for j in range(len(vetor_turnos)):
            evento = matriz_eventos[i][j]
            palestrante = matriz_palestrante[i][j]
            turno = vetor_turnos[j]

            if evento != '':
                print(f'\U0001F552 {turno}: "{evento}" com {palestrante}')
            else:
                print(f'\U0001F552 {turno}: [Sem evento cadastrado]')
        
        print('-' * 40)
        
    print('===========================================\n')
    print('\n')


def buscar_evento():
    print('===========================================')

    while True:
        print('\U0001F4C5 Escolha um dia:')
        print('-' * 40)
        print('Dias:')
        for i, dia in enumerate(vetor_dias):
            print(f'{i} - {dia}')
        try:
            linha = int(input('Informe o número do dia: '))
            if 0 <= linha < len(vetor_dias):
                break 
            else:
                print('\u274C  Dia inválido! Escolha outro.\n')
        except ValueError:
            print('\u274C  Entrada inválida! Digite um número.\n')

    while True:
        print('\n\U0001F552 Escolha um turno:')
        print('-' * 40)
        print('Turnos:')
        for j, turno in enumerate(vetor_turnos):
            print(f'{j} - {turno}')
        try:
            coluna = int(input('Informe o número do turno: '))
            if 0 <= coluna < len(vetor_turnos):
                break  
            else:
                print('\u274C  Turno inválido!')
        except ValueError:
            print('\u274C  Entrada inválida! Digite um número.')

    evento = matriz_eventos[linha][coluna]
    palestrante = matriz_palestrante[linha][coluna]

    print('\n\U0001F4C4 RESULTADO DA BUSCA:')
    if evento != '':
        print(f'\U0001F4DD Evento: {evento}')
        print(f'\U0001F3A4 Palestrante: {palestrante}\n')
    else:
        print(f'\u26A0\ufe0f  Nenhum evento encontrado em {vetor_dias[linha]} ({vetor_turnos[coluna]})\n')
        
    print('===========================================\n')
    print('\n')


def atualizar_evento():
    dias_com_eventos = []  

    for i, dias in enumerate(matriz_eventos):
        if any(turno != '' for turno in dias):
            dias_com_eventos.append(i)  

    print('===========================================')
    print('\U0001F4C5 Primeiramente, escolha um dia:')
    print('-' * 40)
    print('Dias com eventos:')

    for i in dias_com_eventos:
        print(f'{i} - {vetor_dias[i]}')

    while True:
        try:
            dia_selecionado = int(input('Escolha o número do dia: '))

            if dia_selecionado not in dias_com_eventos:
                print('\u274C Dia inválido! Escolha outro.\n')
            else:
                break  
        except ValueError:
            print('\u274C Entrada inválida! Digite um número.\n')
    
     
    turnos_com_eventos = []
    
    for i, evento in enumerate(matriz_eventos[dia_selecionado]):
        if evento != '':
            turnos_com_eventos.append(i)

    
    print('\n\U0001F553 Agora, escolha o turno:')
    print('-' * 40)
    print('Turnos com eventos:')
    
    for j in turnos_com_eventos:
        print(f'{j} - {vetor_turnos[j]}')
        
    while True:
        try:
            turno_selecionado = int(input('Escolha o número do turno: '))

            if turno_selecionado not in turnos_com_eventos:
                print('\u274C Turno inválido! Escolha outro.\n')
            else:
                break  
        except ValueError:
            print('\u274C Entrada inválida! Digite um número.\n')
            
    while True:
        novo_evento = input('\nDigite o nome do evento: ').strip() 
        novo_palestrante = input('Digite o nome do palestrante: ').strip()

        if novo_evento == '' or novo_palestrante == '':
            print('\u2757 Evento ou palestrante não podem ser vazios.')  
        else:
            break  
        
    while True:
        confirmacao = input('Confirma atualizar o evento? (S/N): ').strip().upper()
        
        if confirmacao == 'S':
            matriz_eventos[dia_selecionado][turno_selecionado] = novo_evento
            matriz_palestrante[dia_selecionado][turno_selecionado] = novo_palestrante
            
            print(f'\n\u2705 Evento "{novo_evento}" com palestrante "{novo_palestrante}" atualizado em {vetor_dias[dia_selecionado]} no turno {vetor_turnos[turno_selecionado]}.\n')
            print('===========================================\n')
            break
        
        elif confirmacao == 'N':
            print('\n\u2757 Atualização cancelada pelo usuário.\n')
            print('===========================================\n')
            print('\n')
            break
        
        else:
            print('Por favor, responda com S para sim ou N para não.\n')


def relatorio_por_filtro():
    while True:  
        print('===========================================')
        print('\U0001F4C8 RELATÓRIO COM FILTRO')
        print('Escolha o filtro desejado:')
        print('1 - Filtrar por dia')
        print('2 - Filtrar por turno')
        print('3 - Buscar por nome do evento')
        print('4 - Buscar por nome do palestrante')
        print('0 - Voltar ao menu')

        opcao = input('Informe sua opção: ')

        if opcao == '1':
            print('\n\U0001F4C5 Dias:')
            for i, dia in enumerate(vetor_dias):
                print(f'{i} - {dia}')

            while True:  
                try:
                    dia_escolhido = int(input('Escolha o número do dia: '))
                    if 0 <= dia_escolhido < len(vetor_dias):
                        print(f'\n\U0001F4C4 RELATÓRIO DO DIA {vetor_dias[dia_escolhido]}')
        
                        for j, turno in enumerate(vetor_turnos):
                            evento = matriz_eventos[dia_escolhido][j]
                            palestrante = matriz_palestrante[dia_escolhido][j]
                            if evento != '':
                                print(f'{turno}: "{evento}" com {palestrante}')
                            else:
                                print(f'{turno}: [Sem evento]')
                        break  
                    else:
                        print('\u274C Dia inválido! Escolha outro.\n')
                except ValueError:
                    print('\u274C Entrada inválida! Digite um número.\n')
            break  

        elif opcao == '2':
            print('\n\U0001F552 Turnos:')
            for j, turno in enumerate(vetor_turnos):
                print(f'{j} - {turno}')

            while True:  
                try:
                    turno_escolhido = int(input('Escolha o número do turno: '))
                    if 0 <= turno_escolhido < len(vetor_turnos):
                        print(f'\n\U0001F4C4 RELATÓRIO DO TURNO {vetor_turnos[turno_escolhido]}')
                        
                        for i, dia in enumerate(vetor_dias):
                            evento = matriz_eventos[i][turno_escolhido]
                            palestrante = matriz_palestrante[i][turno_escolhido]
                            if evento != '':
                                print(f'{dia}: "{evento}" com {palestrante}')
                            else:
                                print(f'{dia}: [Sem evento]')
                        break  
                    else:
                        print('\u274C Turno inválido! Escolha outro.\n')
                except ValueError:
                    print('\u274C Entrada inválida! Digite um número.\n')
            break  

        elif opcao == '3':
            nome_evento = input('\nDigite o nome do evento para buscar: ').strip().lower()
            encontrado = False  
            print('\n\U0001F4C4 RESULTADOS ENCONTRADOS:')

            for i in range(len(vetor_dias)):
                for j in range(len(vetor_turnos)):
                    if matriz_eventos[i][j].lower() == nome_evento:
                        print(f'{vetor_dias[i]} - {vetor_turnos[j]}: "{matriz_eventos[i][j]}" com {matriz_palestrante[i][j]}')
                        encontrado = True
            if not encontrado:
                print('\u26A0\ufe0f  Nenhum evento encontrado com esse nome.\n')
            break  

        elif opcao == '4':
            nome_palestrante = input('\nDigite o nome do palestrante para buscar: ').strip().lower()
            encontrado = False
            print('\n\U0001F4C4 RESULTADOS ENCONTRADOS:')

            for i in range(len(vetor_dias)):
                for j in range(len(vetor_turnos)):
                    if matriz_palestrante[i][j].lower() == nome_palestrante:
                        print(f'{vetor_dias[i]} - {vetor_turnos[j]}: "{matriz_eventos[i][j]}" com {matriz_palestrante[i][j]}')
                        encontrado = True
            if not encontrado:
                print('\u26A0\ufe0f  Nenhum palestrante encontrado com esse nome.\n')
            break  

        elif opcao == '0':
            print('Voltando ao menu...')
            break  

        else:
            print('\u274C Entrada inválida! Digite uma opção de 0 a 4.\n')

    print('===========================================\n')
    print('\n')


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
        print('\u0035\uFE0F\u20E3  - Relatório por filtro')
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
                listar_eventos()
            case '3':
                print('\U0001F50D Opção de busca selecionada.\n')
                buscar_evento()
            case '4':
                print('\U0001F4DD Opção de atualização selecionada.\n')
                atualizar_evento()
            case '5':
                print('\U0001F4DC Opção de relatório selecionada.\n')
                relatorio_por_filtro()

            case _:  
                print('\u274C Opção inválida. Tente novamente.\n')
            
        sleep(2)

menu()