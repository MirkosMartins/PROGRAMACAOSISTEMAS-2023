linArq = []
regis = []
label = {}


def mostraMemoria():
  global regis
  print(regis)


def memoria():
  global regis
  for i in range(10):
    regis.append(0)
  return regis

def executaComando(cmd):
  element = cmd.split(' ')

  if len(element) == 3:

    if element[1] == 'JMP':
      return int(element[2]) - 1 

    if element[1] == 'CALL':
      return int(label[element[2]]) - 1 

    param = element[2].split(',')
    p1 = param[0]
    p2 = param[1]
    posiDest = int(p1[1:])

    if element[1] == 'CMP':
      valorOrigem = regis[int(p2[1:])] if p2.startswith('R') else int(p2)
      if regis[posiDest] == valorOrigem:
        return int(element[0])
      else:
        return int(element[0]) + 1

    if element[1] == 'LOAD':
      if p2.startswith('R'):
        regis[posiDest] = regis[int(p2[1:])]
      else:
        regis[posiDest] = int(p2)

    if element[1] == 'ADD':
      if p2.startswith('R'):
        regis[posiDest] = regis[posiDest] + regis[int(p2[1:])]
      else:
        regis[posiDest] = regis[posiDest] + int(p2)

    if element[1] == 'SUB':
      if p2.startswith('R'):
        regis[posiDest] = regis[posiDest] - regis[int(p2[1:])]
      else:
        regis[posiDest] = regis[posiDest] - int(p2)

    if element[1] == 'MULT':
      if p2.startswith('R'):
        regis[posiDest] = regis[posiDest] * regis[int(p2[1:])]
      else:
        regis[posiDest] = regis[posiDest] * int(p2)

    if element[1] == 'DIV':
      if p2.startswith('R'):
        if regis[int(p2[1:])] != 0:
          regis[posiDest] = regis[posiDest] // regis[int(p2[1:])]
        else:
          print('Divisao por zero. ERRO')
          return -1
      else:
        if int(p2) != 0:
          regis[posiDest] = regis[posiDest] // int(p2)
        else:
          print('Divisao por zero. ERRO')
          return -1

    mostraMemoria()

  if element[1] == 'HALT':
    print('FIM DO PROGRAMA.')
    return -1

  return int(element[0])

def executa():
  try:
    nrLinha = 0
    nomeLinha = 0
    endMain = label['main']

    for l in linArq:
      if l.startswith(endMain):
        nrLinha = executaComando(l)
        break

    while nrLinha != -1:
      if nrLinha is not None:
        nomeLinha = '0' + str(nrLinha + 1) if (nrLinha + 1) <= 9 else str(nrLinha + 1)

      for l in linArq:
        if l.startswith(nomeLinha):
          nrLinha = executaComando(l)
          break

  except IndexError:

    contlabel = 0
    flagMain = False

    for l in linArq:
      element = l.split(' ')
      if len(element) == 1 and element[0].endswith(':'):
        element[0] = element[0].replace(':', '')
        contlabel += 1
        if element[0] == 'main':
          flagMain = True

    if flagMain is False:
      print("Input nao contem main.", Exception.__name__)
      return Exception.__name__

  except KeyError:
    contlabel = 0
    flagMain = False

    for l in linArq:
      elementos = l.split(' ')
      if len(elementos) == 1 and elementos[0].endswith(':'):
        elementos[0] = elementos[0].replace(':', '')
        contlabel += 1
        if elementos[0] == 'main':
          flagMain = True

    if flagMain is False:
      print("Input nao contem main.", Exception.__name__)
      return Exception.__name__


def leArquivo(nomeArq):
  global label
  with open(nomeArq) as arq:
    flagLabel = False
    nomeLabel = None
    for linha in arq:
      elementos = linha.rstrip().split(' ')

      if flagLabel:
        label[nomeLabel] = elementos[0]
        flagLabel = False
      if linha.rstrip().endswith(
          ':'):
        flagLabel = True
        nomeLabel = linha[:len(linha) - 2]
      linArq.append(linha.rstrip())


def mostraLinhas():
  global linArq
  for i in range(len(linArq)):
    print(linArq[i])


def main():
  memoria()
  mostraMemoria()
  i = input('Digite o nome do arquivo: ')
  print('\n')
  leArquivo(i)
  mostraLinhas()
  print(f'\n\nlabels dictionary: {label}')
  executa()


if __name__ == '__main__':
  main()