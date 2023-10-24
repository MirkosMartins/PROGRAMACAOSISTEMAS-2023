#LOAD = CARREGA O VALOR | R1 <-- R0 (R1,R0)
#STORE = ARMAZENA DE MODO PERMANENTE R0 | <-- R1 (R0, R1)
#ADD = POSSIBILITA ADICIONAR UM VALOR E SOMAR COM OUTRO (R0, R1) = (R0+R1 EM R0) 

#PROCESSADOR EXPERIMENTAL

registros = []

def mostraMemoria():
    global registros
    print(registros)

def memoria():
    global registros
    for i in range(10):
        registros.append(0)
    return registros

memoria()  # Constrói a memória
cmd = ''

while cmd != 'HALT':
    cmd = input('\nDigite o comando: ')
    elementos = cmd.split(' ')
    if len(elementos) == 2:
        param = elementos[1].split(',')
        p1 = param[0]
        p2 = param[1]

        if elementos[0] == 'LOAD':  # Implementação do LOAD (ADICIONA)
            if p2.startswith('R'):
                posicaoOrigem = int(p2[1:])
                posicaoDestino = int(p1[1:])
                registros[posicaoDestino] = registros[posicaoOrigem]
                mostraMemoria()
            else:
                posicao = int(p1[1:])
                registros[posicao] = int(p2)
                mostraMemoria()

        elif elementos[0] == 'ADD': #Implementação da SOMA
            if p2.startswith('R'):
                posicaoOrigem = int(p2[1:])
                posicaoDestino = int(p1[1:])
                registros[posicaoDestino] += registros[posicaoOrigem]
                mostraMemoria()
            else:
                posicao = int(p1[1:])
                registros[posicao] += int(p2)
                mostraMemoria()

        # Implementação da SUBTRAÇÃO
        elif elementos[0] == 'SUB':
            if p2.startswith('R'):
                posicaoOrigem = int(p2[1:])
                posicaoDestino = int(p1[1:])
                registros[posicaoDestino] -= registros[posicaoOrigem]
                mostraMemoria()
            else:
                posicao = int(p1[1:])
                registros[posicao] -= int(p2)
                mostraMemoria()

        # Implementação da MULTIPLICAÇÃO
        elif elementos[0] == 'MULT':
            if p2.startswith('R'):
                posicaoOrigem = int(p2[1:])
                posicaoDestino = int(p1[1:])
                registros[posicaoDestino] *= registros[posicaoOrigem]
                mostraMemoria()
            else:
                posicao = int(p1[1:])
                registros[posicao] *= int(p2)
                mostraMemoria()

        # Implementação da DIVISÃO
        elif elementos[0] == 'DIV':
            if p2.startswith('R'):
                posicaoOrigem = int(p2[1:])
                posicaoDestino = int(p1[1:])
                if registros[posicaoOrigem] == 0:
                    print("\nERRO: Divisão por zero.")
                else:
                    registros[posicaoDestino] //= registros[posicaoOrigem]
                mostraMemoria()
            else:
                posicao = int(p1[1:])
                divisor = int(p2)
                if divisor == 0:
                    print("\nERRO: Divisão por zero.")
                else:
                    registros[posicao] //= divisor
                mostraMemoria()

    print('\nComando:', elementos[0], '\nParam:', elementos[1])
