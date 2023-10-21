regis = []

def mostra_memoria():
    global regis
    print(regis)

def memoria():
    global regis

    for i in range(10):
        regis.append(0)

    return regis

cmd = ""

memoria()

while cmd != 'HALT':
    cmd = input('Digite o comando: ')
    element = cmd.split(' ')

    if len(element) == 2:
        param = element[1].split(',')
        p1 = param[0]
        p2 = param[1]

        if element[0] == 'LOAD':
            if p2.startswith('R'):
                posicao_inicial = int(p2[1:])
                posicao_final = int(p1[1:])
                regis[posicao_final] = regis[posicao_inicial]
                mostra_memoria()
            else:
                posicao = int(p1[1:])
                regis[posicao] = int(p2)
                mostra_memoria()
        elif element[0] == 'ADD':
            if p2.startswith('R'):
                posicaoinicial = int(p2[1:])
                posicaofinal = int(p1[1:])
                regis[posicaoFinal] += regis[posicaoInicial]
                mostra_memoria()
            else:
                posicao = int(p1[1:])
                regis[posicao] += int(p2)
                mostra_memoria()

    print('comando: ', element[0], 'param: ', element[1])