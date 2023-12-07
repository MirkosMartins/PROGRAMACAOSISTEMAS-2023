linhasArquivo = []
registros = []
labels = {}


def mostraMemoria():
    # Função que imprime o conteúdo da memória (lista de registros)
    global registros
    print(registros)

def memoria():
    # Função que constrói a memória com 10 registradores, todos inicializados como 0
    global registros
    for i in range(10):
        registros.append(0)
    return registros

def executaComando(cmd):
    # Função que executa um comando fornecido como string
    elementos = cmd.split(' ')

    if len(elementos) == 3:
        # Execução de comandos de desvio condicional (JUMP e CALL)
        if elementos[1] == 'JUMP':
            return int(elementos[2]) - 1
        if elementos[1] == 'CALL':
            return int(labels[elementos[2]]) - 1 

        # Processamento de parâmetros e posição de destino
        param = elementos[2].split(',')
        p1 = param[0]
        p2 = param[1]
        posicaoDestino = int(p1[1:])

        # Comando de comparação (CMP)
        if elementos[1] == 'CMP':  
            valorOrigem = registros[int(p2[1:])] if p2.startswith('R') else int(p2)
            if registros[posicaoDestino] == valorOrigem: 
                return int(elementos[0])
            else:
                return int(elementos[0]) + 1

        # Execução de diferentes operações com base no tipo de instrução
        if elementos[1] == 'LOAD':
            if p2.startswith('R'):
                registros[posicaoDestino] = registros[int(p2[1:])]
            else:
                registros[posicaoDestino] = int(p2)

        if elementos[1] == 'ADD':
            if p2.startswith('R'):
                registros[posicaoDestino] = registros[posicaoDestino] + registros[int(p2[1:])]
            else:
                registros[posicaoDestino] = registros[posicaoDestino] + int(p2)

        if elementos[1] == 'SUB':
            if p2.startswith('R'):
                registros[posicaoDestino] = registros[posicaoDestino] - registros[int(p2[1:])]
            else:
                registros[posicaoDestino] = registros[posicaoDestino] - int(p2)

        if elementos[1] == 'MULT':
            if p2.startswith('R'):
                registros[posicaoDestino] = registros[posicaoDestino] * registros[int(p2[1:])]
            else:
                registros[posicaoDestino] = registros[posicaoDestino] * int(p2)

        if elementos[1] == 'DIV':
            if p2.startswith('R'):
                if registros[int(p2[1:])] != 0:
                    registros[posicaoDestino] = registros[posicaoDestino] // registros[int(p2[1:])]
                else:
                    print('Divisao por zero. ERRO')
                    return -1
            else:
                if int(p2) != 0:
                    registros[posicaoDestino] = registros[posicaoDestino] // int(p2)
                else:
                    print('Divisao por zero. ERRO')
                    return -1

        mostraMemoria()

    if elementos[1] == 'HALT':
        # Comando de parada do programa
        print('============')
        return -1

    return int(elementos[0])

def executa():
    # Função principal que executa o programa
    try:
        nrLinha = 0
        nomeLinha = 0
        endMain = labels['main']

        #inicia a execução a partir do rótulo 'main'
        for l in linhasArquivo:
            if l.startswith(endMain):
                nrLinha = executaComando(l)
                break

        #continua a execução até encontrar um comando que pare
        while nrLinha != -1:
            if nrLinha is not None:
                nomeLinha = '0' + str(nrLinha + 1) if (nrLinha + 1) <= 9 else str(nrLinha + 1)

            for l in linhasArquivo:
                if l.startswith(nomeLinha):
                    nrLinha = executaComando(l)
                    break

    except IndexError:
        #trata erros de índices fora de alcance
        contlabels = 0
        flagMain = False

        for l in linhasArquivo:
            elementos = l.split(' ')
            if len(elementos) == 1 and elementos[0].endswith(':'):
                elementos[0] = elementos[0].replace(':', '')
                contlabels += 1
                if elementos[0] == 'main':
                    flagMain = True

        if flagMain is False:
            print("Input nao contem main.", Exception.__name__)
            return Exception.__name__

    except KeyError:
        #trata erros de chaves não encontradas no dicionário
        contlabels = 0
        flagMain = False

        for l in linhasArquivo:
            elementos = l.split(' ')
            if len(elementos) == 1 and elementos[0].endswith(':'):
                elementos[0] = elementos[0].replace(':', '')
                contlabels += 1
                if elementos[0] == 'main':
                    flagMain = True

        if flagMain is False:
            print("Input nao contem main.", Exception.__name__)
            return Exception.__name__


def leArquivo(nomeArquivo):
    # Função q lê o arquiv e preenche: (linhasArquivo) e o dicionário de rótulos(labels)
    global labels
    with open(nomeArquivo) as arquivo:
        flagLabel = False  # Flag de leitura de rótulo, inicia como falso
        nomeLabel = None
        for linha in arquivo:
            elementos = linha.rstrip().split(' ')

            if flagLabel:
                labels[nomeLabel] = elementos[0]
                flagLabel = False
            if linha.rstrip().endswith(':'):
                flagLabel = True
                nomeLabel = linha[:len(linha) - 2]
            linhasArquivo.append(linha.rstrip())


def mostraLinhas():
    #imprime todas as linhas do arquivo
    global linhasArquivo
    for i in range(len(linhasArquivo)):
        print(linhasArquivo[i])


def main():
    
    memoria()  # Constrói a memória
    mostraMemoria()
    i = input('Digite o nome do arquivo: ')
    print('\n')
    leArquivo(i)
    mostraLinhas()
    print(f'\n\nDicionário: {labels}')
    executa()


if __name__ == '__main__':
  main()
