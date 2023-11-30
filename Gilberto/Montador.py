linhas_programa = []
registradores = []
labels = {}


def exibir_memoria():
  global registradores
  print(registradores)


def inicializar_memoria():
  global registradores
  for i in range(10):
    registradores.append(0)
  return registradores


def executar_instrucao(cmd):
  elementos = cmd.split(' ')
  global linhas_programa

  if len(elementos) == 3:
    if elementos[1] == 'CALL':
      flagLabel = False
      label = elementos[2]

      for f in linhas_programa:
        e = f.split(' ')
        if labels[label] in f:
          flagLabel = True

        if flagLabel:
          if len(e) == 1 and label not in e:
            break
          else:
            executar_instrucao(f)

      return int(elementos[0])

    if elementos[1] == 'JUMP':
      for c in linhas_programa:
        e = c.split(' ')
        if elementos[2] == e[0]:
          executar_instrucao(c)
      return int(elementos[0])

    param = elementos[2].split(',')
    p1 = param[0]
    p2 = param[1]
    posicaoDestino = int(p1[1:])

    if elementos[1] == 'CMP':
      cmp = False
      if p2.startswith('R'):
        if registradores[posicaoDestino] == registradores[int(p2[1:])]:
          cmp = True
      else:
        if registradores[posicaoDestino] == int(p2):
          cmp = True

      print(f'{cmd}: {cmp}')

      if not cmp:
        return int(elementos[0]) + 1

      return int(elementos[0])

    if elementos[1] == 'LOAD':
      if p2.startswith('R'):
        registradores[posicaoDestino] = registradores[int(p2[1:])]
      else:
        registradores[posicaoDestino] = int(p2)

    if elementos[1] == 'ADD':
      if p2.startswith('R'):
        registradores[posicaoDestino] = registradores[
            posicaoDestino] + registradores[int(p2[1:])]
      else:
        registradores[posicaoDestino] = registradores[posicaoDestino] + int(p2)

    if elementos[1] == 'SUB':
      if p2.startswith('R'):
        registradores[posicaoDestino] = registradores[
            posicaoDestino] - registradores[int(p2[1:])]
      else:
        registradores[posicaoDestino] = registradores[posicaoDestino] - int(p2)

    if elementos[1] == 'MULT':
      if p2.startswith('R'):
        registradores[posicaoDestino] = registradores[
            posicaoDestino] * registradores[int(p2[1:])]
      else:
        registradores[posicaoDestino] = registradores[posicaoDestino] * int(p2)

    if elementos[1] == 'DIV':
      if p2.startswith('R'):
        if registradores[int(p2[1:])] != 0:
          registradores[posicaoDestino] = registradores[
              posicaoDestino] / registradores[int(p2[1:])]
        else:
          print('A divisão não pode ser por zero.')
          return -1
      else:
        if int(p2) != 0:
          registradores[posicaoDestino] = registradores[posicaoDestino] / int(
              p2)
        else:
          print('A divisão não pode ser por zero.')
          return -1

    inicializar_memoria()

    if elementos[1] == 'HALT':
      print('FIM DO PROGRAMA.')
      return -1

    return int(elementos[0])


def executar_programa():

  try:
    numero_linha = 0
    
    fim_principal = labels['principal']

    for linha in linhas_programa:
      if linha.startswith(fim_principal):
        numero_linha = executar_instrucao(linha)
        break

    while numero_linha != -1:
      nome_linha = '0' + str(numero_linha +
                             1) if numero_linha <= 9 else str(numero_linha + 1)
      for linha in linhas_programa:
        if linha.startswith(nome_linha):
          numero_linha = executar_instrucao(linha)
          break

  except IndexError:
    print("Erro: Índice fora do alcance.")

  except KeyError:
    print("Erro: KeyError. Input não contém a label 'principal'.")


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
      linhas_programa.append(linha.rstrip())


def exibir_linhas():
  global linhas_programa
  for i in range(len(linhas_programa)):
    print(linhas_programa[i])


def main():
  inicializar_memoria()
  exibir_memoria()
  arquivo_input = input('Digite o nome do arquivo: ')
  print('\n')
  ler_arquivo(arquivo_input)
  exibir_linhas()
  print('\n')
  print(f'Dicionário de labels: {labels}')
  executar_programa()


if __name__ == '__main__':
  main()
