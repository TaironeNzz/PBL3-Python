#Autor: Tairone de Jesus Lima
#Componente curricular: MI algoritmos 1
#Concluído em: 06/12/2024
#Eu declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# BIBLIOTECAS:
from Funcoes import dicas_aleatorias
from Funcoes import dicas
import random
import os
import json
import time

# FUNÇÃO PARA TRATAMENTO DE ERRO:
def verificar_entrada():
    estado = True
    while estado:
        try:
            resp = int(input("Sua resposta (digite 6 para sair): "))
            print()
            if resp < 1 or resp > 9:
                print("Por favor, escolha uma resposta entre 1 e 9.")
            else:
                estado = False
        except ValueError:
            print("Digite um número válido!")
    return resp

# FUNÇÃO PARA CARREGAR O ARQUIVO DO HALL DA FAMA:
def carregar_hall():
    with open('halldafama.JSON', 'r', encoding='utf-8') as hall:
        return json.load(hall)

# FUNÇÃO PARA CARREGAR O ARQUIVO DE PERGUNTAS:
def carregar_perguntas():
    with open('quiz1.JSON', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)
    
# FUNÇÃO PARA MODIFICAR O ARQUIVO DO HALL DA FAMA:
def editar_hall(hall_fama_ordenado):
    with open('halldafama.JSON', 'w', encoding='utf-8') as hall:
        json.dump(hall_fama_ordenado,hall,indent=4)
    

# VARIÁVEIS PARA GUARDAR OS DADOS DOS ARQUIVOS:   
hall_fama = carregar_hall()
questoes = carregar_perguntas()

# CÓDIGO PARA PEDIR O NOME DO USUÁRIO:
print("\nOLÁ, SEJA BEM VINDO AO ASK ME\n\nPARA INICIAR O JOGO:\n")
caracter = True
while caracter:
    nome_jogador = input("-> DIGITE SEU NOME (NO MÁXIMO 15 CARACTERES): ")
    if len(nome_jogador) > 15:
        print("\nDIGITE UM NOME COM NO MÁXIMO 15 CARACTERES!")
    else:
        caracter = False

# LOOP PARA INICIAR O JOGO:
loop = True
while loop:

    # MENU DO JOGO:
    os.system('cls')
    print("-------------------------------------------")
    print("|        > BEM VINDO AO ASK ME <          |")
    print("|                                         |")
    print("| [1] MODO LIVRE                          |")
    print("| [2] MODO DE TEMPO                       |")
    print("| [3] MODO NÃO ERRE UMA                   |")
    print("| [4] HALL DA FAMA                        |")
    print("| [5] SAIR                                |")
    print("|                                         |")
    print(f"| PLAYER: {nome_jogador:<15}                 |")
    print("|                                         |")
    print("| DIGITE UM DOS NÚMEROS ACIMA             |")
    print("-------------------------------------------")

    #TRATAMENTO DE ERRO, CASO O USUÁRIO DIGITE UMA LETRA OU UM NÚMERO QUE NÃO CORRESPONDE A UMA OPÇÃO DO MENU:
    situacao = True
    while situacao:
        try:
            n = int(input("Sua escolha: "))
            if n < 1 or n > 5:
                print("Por favor, digite um número entre 1 e 5.")
            else:
                situacao = False
        except ValueError:
            print('Digite um número válido!')

    # VARIÁVEIS PARA SEPARAR A QUANTIDADE DE PERGUNTAS PARA CADA MODO:
    questoesmodo1, questoesmodo2, questoesmodo3 = [],[],[]
    questoesmodo1 = random.sample(questoes,20)
    questoesmodo2 = random.sample(questoes,20)
    questoesmodo3 = random.sample(questoes,20)

    pontuacao = 0
    dica = 1
    pular = 1
    remover = 1
    certas = 0
    contador = 0
    indice = 0
    seguidos = 0

    # INICIA O PRIMEIRO MODO DE JOGO, CASO O USUÁRIO DIGITE O NÚMERO 1:
    if n == 1:
        # FOR PARA IMPRIMIR QUESTÃO POR QUESTÃO:
        for questao in (questoesmodo1):
            indice += 1
            os.system('cls')
            print(f'Categoria: {questao["category"]:<30}Valor: {questao["value"]:<20}Pontuação: {pontuacao:<20}Certas {certas}/{indice}/{"20":<12}Acertos seguidos: {seguidos}')
            print()
            print(f'Pergunta: {questao["questionText"]}')
            print()
            print(f'[1] {questao["option1"]:<100}Ajudas:')
            print(f'[2] {questao["option2"]:<100}')
            print(f'[3] {questao["option3"]:<100}[7] DICA ({dica})')
            print(f'[4] {questao["option4"]:<100}[8] PULAR QUESTÃO ({pular})')
            print(f'[5] {questao["option5"]:<100}[9] REMOVER 3 QUESTÕES ({remover})')
            print()

            # FUNÇÃO PARA USAR AJUDA, CASO O USUÁRIO DIGITE O NÚMERO 7,8 OU 9:
            resp = verificar_entrada()
            if resp == 7 or resp == 8 or resp == 9:
                resp,questoesmodo1,dica,pular,remover,indice,seguidos = dicas(resp,questoesmodo1,questao,dica,pular,remover,indice,pontuacao,certas,seguidos)

            # VERIFICAÇÃO SE A RESPOSTA DO USUÁRIO É A CERTA:
            if f"option{resp}" == questao["answer"]:
                print(f"Resposta correta. {questao["explanation"]}")
                pontuacao += int(questao["value"])
                certas += 1
                contador += 1
                seguidos += 1

            # SAI SE CASO O USUÁRIO DIGITE O NÚMERO 6:
            elif resp == 6:
                print('Saindo...')
                time.sleep(1)
                break

            # VERIFICAÇÃO SE A RESPOSTA DO USUÁRIO É A ERRADA:
            elif resp > 0 and resp < 6 and f"option{resp}" != questao["answer"]:
                print(f"Resposta incorreta! {questao["explanation"]}")
                contador = 0
                seguidos = 0

            # VERIFICA SE O CONTADOR É IGUAL A 6, SE SIM, CHAMA A FUNÇÃO QUE DÁ UMA AJUDA ALEATÓRIA:
            if contador == 6:
                dica,pular,remover = dicas_aleatorias(dica,pular,remover)
                contador = 0

            # DÁ UM TEMPINHO PRO USUÁRIO VER A EXPLICAÇÃO DA RESPOSTA CORRETA:
            if resp != 8:
                time.sleep(2)

        # FUNÇÃO PARA LIMPAR O TERMINAL:
        os.system('cls')
        # VERIFICA SE O USUÁRIO ACERTOU TODAS AS QUESTÕES E MOSTRA A PONTUAÇÃO E A QUANTIDADE DE RESPOSTAS CORRETAS:
        if certas == 20:
            print("PARABÉNS, VOCÊ ACERTOU TODAS AS QUESTÔES!\n\n")
            print(f"VOCÊ ACERTOU {certas} PERGUNTAS E A SUA PONTUAÇÃO É {pontuacao} PONTOS!\n")

        elif indice == 20:
            print("PARABÉNS POR RESPONDER TODAS AS QUESTÔES!\n\n")
            print(f"VOCÊ ACERTOU {certas} PERGUNTAS E A SUA PONTUAÇÃO É {pontuacao} PONTOS!\n")

        for modo in hall_fama:
            if "livre" in modo:  # VERIFICA SE A CHAVE LIVRE ESTÁ NO ARQUIVO DO HALL DA FAMA 
                nomes = modo["livre"].items()  # PEGA AS CHAVES E OS VALORES DA CHAVE LIVRE
                p = False # SERVE PARA IMPRIMIR QUE O USUÁRIO NÃO ENTROU NO HALL
                for nome, pontuacao_armazenada in nomes: # FOR PARA VERIFICAR OS PONTOS
                    if nome_jogador == nome and pontuacao > pontuacao_armazenada:  # VERIFICA SE A PONTUAÇÃO É MAIOR E SE O NOME FOR IGUAL
                        print("PARABÉNS, VOCÊ AUMENTOU SUA PONTUAÇÃO!\n")
                        modo["livre"][nome] = pontuacao # TROCA A PONTUAÇÃO
                        p = True
                        break
                    elif nome_jogador == nome and pontuacao < pontuacao_armazenada: # VERIFICA SE A PONTUAÇÃO É MENOR, SE FOR, QUEBRA O LOOP
                        p = False
                        break
                    elif  nome_jogador == nome and pontuacao == pontuacao_armazenada: # VERIFICA SE A PONTUAÇÃO É IGUAL, SE FOR, QUEBRA O LOOP
                        p = False
                        break
                    elif nome_jogador != nome and pontuacao > pontuacao_armazenada: # VERIFICA O NOME E SE A PONTUAÇÃO É MAIOR, SE FOR ADICIONA NO HALL OU SUBSTITUI A PONTUAÇÃO NO HALL
                        if nome_jogador in modo["livre"]: # VERIFICA SE O NOME ESTÁ NO HALL DA FAMA
                            modo["livre"][nome_jogador] = pontuacao # SE TIVER, ELE TROCA A PONTUAÇÃO
                            print("PARABÉNS, VOCÊ SUBIU DE RANKING NO HALL DA FAMA!\n")
                            p = True
                            break

                        print("PARABÉNS, VOCÊ ENTROU NO HALL DA FAMA!\n") # SE CASO O NOME NÃO ESTIVER, ELE ADICIONA NO HALL DA FAMA
                        modo["livre"].popitem() # REMOVE A ULTIMA CHAVE E O VALOR
                        modo["livre"][nome_jogador] = pontuacao # ADICIONA O NOME COM A PONTUAÇÃO 
                        p = True
                        break  # SAI DO LOOP

                if p == False: # SE NÃO TER PONTO PARA ENTRAR NO HALL, IMPRIMI ESSA MENSAGEM
                    print("INFELIZMENTE VOCÊ NÂO ENTROU NO HALL DA FAMA :(\n")

                modo["livre"] = dict(sorted(modo["livre"].items(), key=lambda x: x[1], reverse=True)) # FUNÇÃO PARA ORDENAR O DICIONÁRIO DE ACORDO COM OS PONTOS
        
        editar_hall(hall_fama) # FUNÇÃO PARA MODIFICAR O ARQUIVO DO HALL DA FAMA
        input("Pressione qualquer tecla para sair: ")

    # INICIA O SEGUNDO MODO DE JOGO, CASO O USUÁRIO DIGITE O NÚMERO 2:
    elif n == 2:
        tempo_limite = 300
        inicio = time.time()

        for questao in (questoesmodo2):
                fim = time.time()
                tempo = int(fim - inicio)
                if tempo >= tempo_limite:
                    os.system('cls')
                    print(f"SEU TEMPO ACABOU!\n\n")
                    if certas > 0:
                        print(f"VOCÊ ACERTOU {certas - 1} PERGUNTAS EM {tempo_limite} SEGUNDOS.\n")
                    else:
                        print(f"VOCÊ ACERTOU {certas} PERGUNTAS EM {tempo_limite} SEGUNDOS.\n")
                    break

                indice += 1
                os.system('cls')
                print(f'Categoria: {questao["category"]:<30}Valor: {questao["value"]:<20}Pontuação: {pontuacao:<20}Certas {certas}/{indice}/{"20":<12}Acertos seguidos: {seguidos}')
                print()
                print(f'Pergunta: {questao["questionText"]}')
                print()
                print(f'[1] {questao["option1"]:<100}Ajudas:')
                print(f'[2] {questao["option2"]:<100}')
                print(f'[3] {questao["option3"]:<100}[7] DICA ({dica})')
                print(f'[4] {questao["option4"]:<100}[8] PULAR QUESTÃO ({pular})')
                print(f'[5] {questao["option5"]:<100}[9] REMOVER 3 QUESTÕES ({remover})')
                print()
                print(f"Tempo restante: {tempo_limite - tempo} segundos!\n")
    
                resp = verificar_entrada()
                if resp == 7 or resp == 8 or resp == 9:
                    resp,questoesmodo1,dica,pular,remover,indice,seguidos = dicas(resp,questoesmodo2,questao,dica,pular,remover,indice,pontuacao,certas,seguidos)

                if f"option{resp}" == questao["answer"]:
                    print(f"Resposta correta. {questao["explanation"]}")
                    pontuacao += int(questao["value"])
                    certas += 1
                    contador += 1
                    seguidos += 1

                elif resp == 6:
                    print('Saindo...')
                    time.sleep(1)
                    break

                elif resp > 0 and resp < 6 and f"option{resp}" != questao["answer"]:
                    print(f"Resposta incorreta! {questao["explanation"]}")
                    contador = 0
                    seguidos = 0

                if contador == 6:
                    dica,pular,remover = dicas_aleatorias(dica,pular,remover)
                    contador = 0
                if resp != 8:
                    time.sleep(0.5)

        os.system('cls')
        # VERIFICA SE O USUÁRIO ACERTOU TODAS AS QUESTÕES E MOSTRA O TEMPO E A QUANTIDADE DE RESPOSTAS CORRETAS:
        if certas == 20:
            print("PARABÉNS, VOCÊ ACERTOU TODAS AS QUESTÔES!\n\n")
            print(f"VOCÊ ACERTOU {certas} PERGUNTAS EM {tempo} SEGUNDOS!\n")

        elif indice == 20:
            print("PARABÉNS POR RESPONDER TODAS AS QUESTÔES!\n\n")
            print(f"VOCÊ ACERTOU {certas} PERGUNTAS EM {tempo} SEGUNDOS!\n")

        if certas >= 10: # SÓ ENTRA PARA COMPARAR O TEMPO SE O USUÁRIO ACERTAS PELO MENOS 10 PERGUNTAS
            for modo in hall_fama:
                if "tempo" in modo:  # VERIFICA SE A CHAVE LIVRE ESTÁ NO ARQUIVO DO HALL DA FAMA 
                    nomes = modo["tempo"].items()  # PEGA AS CHAVES E OS VALORES DA CHAVE LIVRE
                    p = False # SERVE PARA IMPRIMIR QUE O USUÁRIO NÃO ENTROU NO HALL
                    for nome, pontuacao_armazenada in nomes: # FOR PARA VERIFICAR OS PONTOS
                        if nome_jogador == nome and tempo < pontuacao_armazenada:  # VERIFICA SE O TEMPO É MENOR E SE O NOME FOR IGUAL
                            print("PARABÉNS, VOCÊ AUMENTOU SUA PONTUAÇÃO!\n")
                            modo["tempo"][nome] = tempo # TROCA A PONTUAÇÃO
                            p = True
                            break
                        elif nome_jogador == nome and tempo > pontuacao_armazenada: # VERIFICA SE O TEMPO É MAIOR, SE FOR, QUEBRA O LOOP
                            p = False
                            break
                        elif  nome_jogador == nome and tempo == pontuacao_armazenada: # VERIFICA SE O TEMPO É IGUAL, SE FOR, QUEBRA O LOOP
                            p = False
                            break
                        elif nome_jogador != nome and tempo < pontuacao_armazenada: # VERIFICA O NOME E SE A TEMPO É MENOR, SE FOR ADICIONA NO HALL OU SUBSTITUI A PONTUAÇÃO NO HALL
                            if nome_jogador in modo["tempo"]: # VERIFICA SE O NOME ESTÁ NO HALL DA FAMA
                                modo["tempo"][nome_jogador] = tempo # SE TIVER, ELE TROCA O TEMPO
                                print("PARABÉNS, VOCÊ SUBIU DE RANKING NO HALL DA FAMA!\n")
                                p = True
                                break

                            print("PARABÉNS, VOCÊ ENTROU NO HALL DA FAMA!") # SE CASO O NOME NÃO ESTIVER, ELE ADICIONA NO HALL DA FAMA
                            modo["tempo"].popitem() # REMOVE A ULTIMA CHAVE E O VALOR
                            modo["tempo"][nome_jogador] = tempo # ADICIONA O NOME COM O TEMPO
                            p = True
                            break  # SAI DO LOOP

                    if p == False: # SE NÃO TER TEMPO PARA ENTRAR NO HALL, IMPRIMI ESSA MENSAGEM
                        print("INFELIZMENTE VOCÊ NÂO MODIFICOU O HALL DA FAMA :(\n")

                    modo["tempo"] = dict(sorted(modo["tempo"].items(), key=lambda x: x[1], reverse=False)) # FUNÇÃO PARA ORDENAR O DICIONÁRIO DE ACORDO COM OS PONTOS
            
            editar_hall(hall_fama) # FUNÇÃO PARA MODIFICAR O ARQUIVO DO HALL DA FAMA
            input("Pressione qualquer tecla para sair: ")
        else:
            print("NÃO FOI POSSÍVEL ENTRAR NO HALL DA FAMA PORQUE VOCÊ ACERTOU MENOS QUE 10!\n")
            input("Pressione qualquer tecla para sair: ")

    # INICIA O TERCEIRO MODO DE JOGO, CASO O USUÁRIO DIGITE O NÚMERO 3:
    elif n == 3:

        for questao in (questoesmodo3):
            indice += 1
            os.system('cls')
            print(f'Categoria: {questao["category"]:<30}Valor: {questao["value"]:<20}Pontuação: {pontuacao:<20}Certas {certas}/{indice}/{"20":<12}Acertos seguidos: {seguidos}')
            print()
            print(f'Pergunta: {questao["questionText"]}')
            print()
            print(f'[1] {questao["option1"]:<100}Ajudas:')
            print(f'[2] {questao["option2"]:<100}')
            print(f'[3] {questao["option3"]:<100}[7] DICA ({dica})')
            print(f'[4] {questao["option4"]:<100}[8] PULAR QUESTÃO ({pular})')
            print(f'[5] {questao["option5"]:<100}[9] REMOVER 3 QUESTÕES ({remover})')
            print()

            resp = verificar_entrada()
            if resp == 7 or resp == 8 or resp == 9:
                resp,questoesmodo1,dica,pular,remover,indice,seguidos = dicas(resp,questoesmodo3,questao,dica,pular,remover,indice,pontuacao,certas,seguidos)

            if f"option{resp}" == questao["answer"]:
                print(f"Resposta correta. {questao["explanation"]}")
                pontuacao += int(questao["value"])
                certas += 1
                contador += 1
                seguidos += 1

            elif resp == 6:
                print('Saindo...')
                time.sleep(1)
                break

            # VERIFICAÇÃO SE A RESPOSTA DO USUÁRIO É A ERRADA, SE SIM, ELE PERDE E MOSTRA A PONTUAÇÃO E A QUANTIDADE DE RESPOSTAS CORRETAS:
            elif resp > 0 and resp < 6 and f"option{resp}" != questao["answer"]:
                os.system('cls')
                print(f"VOCÊ PERDEU!\n\nEXPLICAÇÂO: {questao["explanation"]}\n\n")
                print(f"VOCÊ ACERTOU {certas} PERGUNTAS E A SUA PONTUAÇÃO É {pontuacao} PONTOS!\n")
                break

            if contador == 6:
                dica,pular,remover = dicas_aleatorias(dica,pular,remover)
                contador = 0
            if resp != 8:
                time.sleep(2)
        if certas == 20:
            # MENSANGEM DE PARABÉNS AO RESPONDER TODAS AS PERGUNTAS CORRETAMENTE SEM ERRAR UMA:
            print("PARABÉNS, VOCÊ ACERTOU TODAS AS QUESTÔES!\n\n")
            print(f"VOCÊ ACERTOU {certas} PERGUNTAS E A SUA PONTUAÇÃO É {pontuacao} PONTOS!\n")

        for modo in hall_fama:
            if "erre" in modo:  # VERIFICA SE A CHAVE LIVRE ESTÁ NO ARQUIVO DO HALL DA FAMA 
                nomes = modo["erre"].items()  # PEGA AS CHAVES E OS VALORES DA CHAVE LIVRE
                p = False # SERVE PARA IMPRIMIR QUE O USUÁRIO NÃO ENTROU NO HALL
                for nome, pontuacao_armazenada in nomes: # FOR PARA VERIFICAR OS PONTOS
                    if nome_jogador == nome and pontuacao > pontuacao_armazenada:  # VERIFICA SE A PONTUAÇÃO É MAIOR E SE O NOME FOR IGUAL
                        print("PARABÉNS, VOCÊ AUMENTOU SUA PONTUAÇÃO!\n")
                        modo["erre"][nome] = pontuacao # TROCA A PONTUAÇÃO
                        p = True
                        break
                    elif nome_jogador == nome and pontuacao < pontuacao_armazenada: # VERIFICA SE A PONTUAÇÃO É MENOR, SE FOR, QUEBRA O LOOP
                        p = False
                        break
                    elif  nome_jogador == nome and pontuacao == pontuacao_armazenada: # VERIFICA SE A PONTUAÇÃO É IGUAL, SE FOR, QUEBRA O LOOP
                        p = False
                        break
                    elif nome_jogador != nome and pontuacao > pontuacao_armazenada: # VERIFICA O NOME E SE A PONTUAÇÃO É MAIOR, SE FOR ADICIONA NO HALL OU SUBSTITUI A PONTUAÇÃO NO HALL
                        if nome_jogador in modo["erre"]: # VERIFICA SE O NOME ESTÁ NO HALL DA FAMA
                            modo["erre"][nome_jogador] = pontuacao # SE TIVER, ELE TROCA A PONTUAÇÃO
                            print("PARABÉNS, VOCÊ SUBIU DE RANKING NO HALL DA FAMA!\n")
                            p = True
                            break

                        print("PARABÉNS, VOCÊ ENTROU NO HALL DA FAMA!\n") # SE CASO O NOME NÃO ESTIVER, ELE ADICIONA NO HALL DA FAMA
                        modo["erre"].popitem() # REMOVE A ULTIMA CHAVE E O VALOR
                        modo["erre"][nome_jogador] = pontuacao # ADICIONA O NOME COM A PONTUAÇÃO 
                        p = True
                        break  # SAI DO LOOP

                if p == False: # SE NÃO TER PONTO PARA ENTRAR NO HALL, IMPRIMI ESSA MENSAGEM
                    print("INFELIZMENTE VOCÊ NÂO ENTROU NO HALL DA FAMA :(\n")

                modo["erre"] = dict(sorted(modo["erre"].items(), key=lambda x: x[1], reverse=True)) # FUNÇÃO PARA ORDENAR O DICIONÁRIO DE ACORDO COM OS PONTOS
        
        editar_hall(hall_fama) # FUNÇÃO PARA MODIFICAR O ARQUIVO DO HALL DA FAMA
        input("Pressione qualquer tecla para sair: ")

    # MOSTRA O HALL DA FAMA, CASO O USUÁRIO DIGITE O NÚMERO 4:
    elif n == 4:
        e = True
        while e:
            os.system('cls')

            # MENU DO HALL DA FAMA:
            print("-------------------------------------------")
            print("|            > HALL DA FAMA <             |")
            print("|                                         |")
            print("| [1] HALL LIVRE                          |")
            print("| [2] HALL DE TEMPO                       |")
            print("| [3] HALL NÃO ERRE UMA                   |")
            print("| [4] SAIR                                |")
            print("|                                         |")
            print("| DIGITE UM DOS NÚMEROS ACIMA             |")
            print("-------------------------------------------")

            # TRATAMENTO DE ERRO, CASO O USUÁRIO DIGITE UMA LETRA:
            status = True
            while status:
                try:
                    num = int(input("Sua resposta: "))
                    status = False
                except ValueError:
                    print("Digite um número!")
            i = 0

            # MOSTRA O HALL DA FAMA DO MODO LIVRE:
            if num == 1:
                os.system('cls')
                print("MODO LIVRE\n")
                for modo in hall_fama:
                    if "livre" in modo:
                        dados = modo["livre"].items()
                for nome, pontos in dados:
                    print(f"{i+1:<2}º {nome:<15} | PONTOS: {pontos:<3} |")
                    print("-----------------------------------")
                    i += 1
                print()
                sair = input("Pressione qualquer tecla para sair: ")

            # MOSTRA O HALL DA FAMA DO MODO TEMPO:
            elif num == 2:
                os.system('cls')
                print("MODO TEMPO\n")
                for modo in hall_fama:
                    if "tempo" in modo:
                        dados = modo["tempo"].items()
                for nome, pontos in dados:
                    print(f"{i+1:<2}º {nome:<15} | TEMPO: {pontos:<3} seg. |")
                    print("---------------------------------------")
                    i += 1
                print()
                sair = input("Pressione qualquer tecla para sair: ")

            # MOSTRA O HALL DA FAMA DO MODO NÃO ERRE:
            elif num == 3:
                os.system('cls')
                print("MODO NÂO ERRE\n")
                for modo in hall_fama:
                    if "erre" in modo:
                        dados = modo["erre"].items()
                for nome, pontos in dados:
                    print(f"{i+1:<2}º {nome:<15} | PONTOS: {pontos:<3} |")
                    print("-----------------------------------")
                    i += 1
                print()
                sair = input("Pressione qualquer tecla para sair: ")
            
            # SAI DO MENU DO HALL DA FAMA, CASO NÃO SEJA DIGITADO NENHUM NÚMERO CORRESPONDENTE AS OPÇÕES:
            else:
                e = False
    
    # ENCERRA O JOGO, CASO SEJA DIGITADO O NÚMERO 5:
    else:
        os.system('cls')
        print('Finalizando...')
        time.sleep(0.5)
        print('3')
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('1')
        time.sleep(0.5)
        print('encerrado!')
        loop = False
