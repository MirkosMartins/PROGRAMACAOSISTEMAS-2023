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
  elementos = cmd.split(' ')

  if len(elementos) == 3:

    if elementos[1] == 'JUMP':
      return int(elementos[2]) - 1

    if elementos[1] == 'CALL':
      return int(labels[elementos[2]]) - 1 

    param = elementos[2].split(',')
    p1 = param[0]
    p2 = param[1]
    posicaoDestino = int(p1[1:])

    if elementos[1] == 'CMP':  
      valorOrigem = registros[int(p2[1:])] if p2.startswith('R') else int(p2)
      if registros[posicaoDestino] == valorOrigem: 
        return int(elementos[0])
      else:
        return int(elementos[0]) + 1

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
    print('==============================================================')
    return -1

  return int(elementos[0])

def executa():
  try:
    nrLinha = 0
    nomeLinha = 0
    endMain = labels['main']

    for l in linhasArquivo:  # p cada linha do arquivo...
      if l.startswith(endMain):  # se a linha começar com o endereço do main
        nrLinha = executaComando(l)
        break

    while nrLinha != -1:
      if nrLinha is not None:
        nomeLinha = '0' + str(nrLinha + 1) if (nrLinha + 1) <= 9 else str(nrLinha + 1)

      for l in linhasArquivo:
        if l.startswith(nomeLinha):
          nrLinha = executaComando(l)
          break

  except IndexError:  # tratando os 2 erros específicos possíveis

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
  global labels
  with open(nomeArquivo) as arquivo:
    flagLabel = False  # flag de leitura de label por padrão como falso
    nomeLabel = None
    for linha in arquivo:
      elementos = linha.rstrip().split(' ')

      if flagLabel:
        labels[nomeLabel] = elementos[0]
        flagLabel = False
      if linha.rstrip().endswith(
          ':'):  # se o conteudo da linha terminar com ':' (label)
        flagLabel = True
        nomeLabel = linha[:len(linha) - 2]
      linhasArquivo.append(linha.rstrip())


def mostraLinhas():
  global linhasArquivo
  for i in range(len(linhasArquivo)):
    print(linhasArquivo[i])


def main():
  memoria()  #constroi a memoria
  mostraMemoria()
  i = input('Digite o nome do arquivo: ')
  print('\n')
  leArquivo(i)
  mostraLinhas()
  print(f'\n\nlabels dictionary: {labels}')
  executa()


if __name__ == '__main__':
  main()
