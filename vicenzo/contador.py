# -*- coding: utf-8 -*-

linhas_arquivo = []
registros = []
labels = {}


def mostrar_memoria():
    global registros
    print(registros)


def inicializar_memoria():
    global registros
    for _ in range(10):
        registros.append(0)
    return registros


def executar_comando(cmd):
    elementos = cmd.split(' ')

    if len(elementos) == 3:

        if elementos[1] == 'JMP':
            return int(elementos[2]) - 1

        if elementos[1] == 'CALL':
            return int(labels[elementos[2]]) - 1

        param = elementos[2].split(',')
        p1 = param[0]
        p2 = param[1]
        posicao_destino = int(p1[1:])

        if elementos[1] == 'CMP':
            valor_origem = registros[int(p2[1:])] if p2.startswith('R') else int(p2)
            if registros[posicao_destino] == valor_origem:
                return int(elementos[0])
            else:
                return int(elementos[0]) + 1

        if elementos[1] == 'LOAD':
            if p2.startswith('R'):
                registros[posicao_destino] = registros[int(p2[1:])]
            else:
                registros[posicao_destino] = int(p2)

        if elementos[1] == 'ADD':
            if p2.startswith('R'):
                registros[posicao_destino] += registros[int(p2[1:])]
            else:
                registros[posicao_destino] += int(p2)

        if elementos[1] == 'SUB':
            if p2.startswith('R'):
                registros[posicao_destino] -= registros[int(p2[1:])]
            else:
                registros[posicao_destino] -= int(p2)

        if elementos[1] == 'MULT':
            if p2.startswith('R'):
                registros[posicao_destino] *= registros[int(p2[1:])]
            else:
                registros[posicao_destino] *= int(p2)

        if elementos[1] == 'DIV':
            if p2.startswith('R'):
                if registros[int(p2[1:])] != 0:
                    registros[posicao_destino] //= registros[int(p2[1:])]
                else:
                    print('Divisão por zero. ERRO')
                    return -1
            else:
                if int(p2) != 0:
                    registros[posicao_destino] //= int(p2)
                else:
                    print('Divisão por zero. ERRO')
                    return -1

        mostrar_memoria()

    if elementos[1] == 'HALT':
        print('FIM DO PROGRAMA.')
        return -1

    return int(elementos[0])


def executar():
    try:
        nr_linha = 0
        nome_linha = 0
        end_main = labels['main']

        for linha in linhas_arquivo:
            if linha.startswith(end_main):
                nr_linha = executar_comando(linha)
                break

        while nr_linha != -1:
            if nr_linha is not None:
                nome_linha = '0' + str(nr_linha + 1) if (nr_linha + 1) <= 9 else str(nr_linha + 1)

            for linha in linhas_arquivo:
                if linha.startswith(nome_linha):
                    nr_linha = executar_comando(linha)
                    break

    except IndexError:

        cont_labels = 0
        flag_main = False

        for linha in linhas_arquivo:
            elementos = linha.split(' ')
            if len(elementos) == 1 and elementos[0].endswith(':'):
                elementos[0] = elementos[0].replace(':', '')
                cont_labels += 1
                if elementos[0] == 'main':
                    flag_main = True

        if not flag_main:
            print("Main não foi encontrado! ERRO", Exception.__name__)
            return Exception.__name__

    except KeyError:
        cont_labels = 0
        flag_main = False

        for linha in linhas_arquivo:
            elementos = linha.split(' ')
            if len(elementos) == 1 and elementos[0].endswith(':'):
                elementos[0] = elementos[0].replace(':', '')
                cont_labels += 1
                if elementos[0] == 'main':
                    flag_main = True

        if not flag_main:
            print("Main não foi encontrado! ERRO.", Exception.__name__)
            return Exception.__name__


def ler_arquivo(nome_arquivo):
    global labels
    with open(nome_arquivo) as arquivo:
        flag_label = False
        nome_label = None
        for linha in arquivo:
            elementos = linha.rstrip().split(' ')

            if flag_label:
                labels[nome_label] = elementos[0]
                flag_label = False
            if linha.rstrip().endswith(':'):  
                flag_label = True
                nome_label = linha[:len(linha) - 2]
            linhas_arquivo.append(linha.rstrip())


def mostrar_linhas():
    global linhas_arquivo
    for i in range(len(linhas_arquivo)):
        print(linhas_arquivo[i])


def programa_principal():
    inicializar_memoria()
    mostrar_memoria()
    nome_arquivo = input('Digite o nome do arquivo: ')
    print('\n')
    ler_arquivo(nome_arquivo)
    mostrar_linhas()
    print(f'\n\n {labels}')
    executar()


if __name__ == '__main__':
    programa_principal()
