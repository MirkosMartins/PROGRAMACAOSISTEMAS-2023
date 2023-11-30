linhasArquivo = []
registros = []
labels = {}


def mostraMemoria():
    global registros
    print(registros)


def memoria():
    global registros
    for i in range(10):
        registros.append(0)
    return registros


def executaComando(cmd):
    global registros
    elementos = cmd.split(' ')
    if len(elementos) == 3:
        if ',' in elementos[2]:
            param = elementos[2].split(',')
            p1 = param[0]
            p2 = param[1]
            posicaoDestino = int(p1[1:])
            if p2.startswith('R'):
                valorOrigem = registros[int(p2[1:])]
            else:
                valorOrigem = int(p2)
            if elementos[1] == 'LOAD':
                registros[posicaoDestino] = valorOrigem
            elif elementos[1] == 'ADD':
                registros[posicaoDestino] = registros[posicaoDestino] + valorOrigem
            elif elementos[1] == 'SUB':
                registros[posicaoDestino] = registros[posicaoDestino] - valorOrigem
            elif elementos[1] == 'MULT':
                registros[posicaoDestino] = registros[posicaoDestino] * valorOrigem
            elif elementos[1] == 'DIV':
                if valorOrigem != 0:
                    registros[posicaoDestino] = int(registros[posicaoDestino] / valorOrigem)
                else:
                    print('Divisao por zero. ERRO')
                    return -1
            elif elementos[1] == 'CMP':
                # compara os valores e atualiza um registro  ex(, R9)
                if registros[posicaoDestino] == valorOrigem:
                    registros[9] = 0  # valores =, status = 0
                elif registros[posicaoDestino] < valorOrigem:
                    registros[9] = -1  # valor destino é menor, status = -1
                else:
                    registros[9] = 1  # valor destino é maior, status = 1
        else:
            if elementos[1] == 'CALL':
                # chamada, salva o endereço da próxima instrução e pula para a função
                endereco_proxima_instrucao = int(elementos[0]) + 1
                return int(labels[elementos[2]])  # Retorna o endereço da função
            elif elementos[1] == 'JUMP':
                #salta para o endereço especificado
                if elementos[2].startswith('R'):
                    return int(registros[int(elementos[2][1:])])
                else:
                    return int(elementos[2])
        mostraMemoria()
    if elementos[1] == 'HALT':
        print('FIM DO PROGRAMA.')
        return -1
    return int(elementos[0]) + 1


def executa():
    try:
        endMain = labels['main']
        nrLinha = 0
        print(endMain)
        for l in linhasArquivo:
            if l.startswith(endMain):
                nrLinha = executaComando(l)
                break
        while nrLinha != -1:
            if nrLinha < 10:
                nomeLinha = '0' + str(nrLinha)
            else:
                nomeLinha = str(nrLinha)
            for l in linhasArquivo:
                if l.startswith(nomeLinha):
                    print(l, 'linha')
                    nrLinha = executaComando(l)
                    break
    except:
        print('input nao possui main\nFim do programa.', Exception.__name__)


def leArquivo(nomeArquivo):
    global labels
    with open(nomeArquivo) as arquivo:
        flagLabel = False
        nomeLabel = None
        for linha in arquivo:
            elementos = linha.split(' ')
            if flagLabel == True:
                labels[nomeLabel] = elementos[0]
                flagLabel = False
            if linha.rstrip().endswith(':'):
                flagLabel = True
                nomeLabel = linha[:len(linha) - 2]
            linhasArquivo.append(linha.rstrip())
        arquivo.close()


def mostraLinhas():
    global linhasArquivo
    for i in range(len(linhasArquivo)):
        print(linhasArquivo[i])


def main():
    memoria()
    mostraMemoria()
    i = input('Digite o nome do arquivo:')
    leArquivo(i)
    mostraLinhas()
    print(labels)
    executa()


if __name__ == '__main__':
    main()

