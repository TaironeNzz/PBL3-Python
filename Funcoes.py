import random
import os
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

def entrada_inteiros():
    estado = True
    while estado:
        try:
            resp = int(input("Digite seu número: "))
            estado = False
        except ValueError:
            print("Digite um número inteiro!")
    return resp

dica = 0 
pular = 0
remover = 0



def dicas_aleatorias(dica,pular,remover):

    if dica == 0 or pular == 0 or remover == 0:
        resultado = random.randint(1,3)
        if resultado == 1 and dica == 0:
            dica += 1
        elif resultado == 2 and pular == 0:
            pular += 1
        elif resultado == 3 and remover == 0:
            remover += 1
        else:
            return dicas_aleatorias(dica,pular,remover)
    return dica,pular,remover


def dicas(resp,questoesmodo,questao,dica,pular,remover,indice,pontuacao,certas,seguidos):
    n = True
    while n:
        if resp == 7:
            if dica == 1:
                print(f"Dica: {questao["hint"]}")
                print()
                dica -= 1
                resp = verificar_entrada()
            else:
                print("Você não tem dica suficiente!")
                resp = verificar_entrada()
        elif resp == 8:
            if pular == 1:
                pular -= 1
                questoesmodo.append(questao)
                indice -= 1
                n = False
            else:
                print("Você não tem pulos suficientes!")
                resp = verificar_entrada()
        elif resp == 9:
            if remover == 1:
                opcoes = {"option1":questao["option1"],"option2":questao["option2"],"option3":questao["option3"],"option4":questao["option4"],"option5":questao["option5"]}
                opcoes_erradas = [k for k, v in opcoes.items() if k != questao["answer"]]
                opcoes_removidas = random.sample(opcoes_erradas, 3)

                for chave in opcoes_removidas:
                    opcoes[chave] = "" 

                os.system('cls')
                print(f'Categoria: {questao["category"]:<30}Valor: {questao["value"]:<20}Pontuação: {pontuacao:<20}Certas {certas}/{indice}/{"20":<12}Acertos seguidos: {seguidos}')
                print()
                print(f'Pergunta: {questao["questionText"]}')
                print()
                print(f'[1] {opcoes["option1"]:<100}Ajudas:')
                print(f'[2] {opcoes["option2"]:<100}')
                print(f'[3] {opcoes["option3"]:<100}[7] DICA ({dica})')
                print(f'[4] {opcoes["option4"]:<100}[8] PULAR QUESTÃO ({pular})')
                print(f'[5] {opcoes["option5"]:<100}[9] REMOVER 3 QUESTÕES ({remover})')
                print()
                remover -= 1
                resp = verificar_entrada()
            else:
                print("Você não pode remover!")
                resp = verificar_entrada()
        else:
            n = False
    return resp,questoesmodo,dica,pular,remover,indice,seguidos