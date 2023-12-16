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
  linhaAtual = int(elementos[0])
  if len(elementos) == 3:
    print(elementos[1])
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
    if elementos[1] == 'ADD':
      registros[posicaoDestino] = registros[posicaoDestino] + valorOrigem
    if elementos[1] == 'SUB':
      registros[posicaoDestino] = registros[posicaoDestino] - valorOrigem
    if elementos[1] == 'MULT':
      registros[posicaoDestino] = registros[posicaoDestino] * valorOrigem
    if elementos[1] == 'DIV':
      if valorOrigem != 0:
        registros[posicaoDestino] = int(registros[posicaoDestino] /
                                        valorOrigem)
      else:
        print('Divisao por zero. ERRO')
        return -1

    if elementos[1] == 'CMP':
      if registros[posicaoDestino] != valorOrigem:
        linhaAtual += 1
        print(elementos[1], '*****')
    if elementos[1] == 'JUMP':
      print("JUUUUUMP")
      linhaAtual = int(elementos[2])
    mostraMemoria()
  if elementos[1] == 'HALT':
    mostraMemoria()
    print('FIM DO PROGRAMA.')
    return -1
  return linhaAtual


def executa():
  #procura o main
  try:
    endMain = labels['main']
    nrLinha = 0
    print(endMain)
    for l in linhasArquivo:
      if l.startswith(endMain):
        nrLinha = executaComando(l)
        break
    while nrLinha != -1:
      if nrLinha < 9:
        nomeLinha = '0' + str(nrLinha + 1)
      else:
        nomeLinha = str(nrLinha + 1)
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
  memoria()  #constroi a memoria
  mostraMemoria()
  i = input('Digite o nome do arquivo:')
  leArquivo(i)
  mostraLinhas()
  print(labels)
  executa()


if __name__ == '__main__':
  main()