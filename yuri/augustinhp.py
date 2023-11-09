registros = [0] * 10


def mostra_memoria():
  global registros
  print(registros)


def memoria():
  global registros
  registros = [0] * 10


def executar_comando(comando):
  global registros

  elementos = comando.split(' ')
  if len(elementos) == 2:
    param = elementos[1].split(',')
    p1 = param[0]
    p2 = param[1]

    if elementos[0] == 'LOAD':
      if p2.startswith('R'):
        posicao_origem = int(p2[1:])
        posicao_destino = int(p1[1:])
        registros[posicao_destino] = registros[posicao_origem]
      else:
        posicao = int(p1[1:])
        registros[posicao] = int(p2)

    elif elementos[0] == 'ADD':
      if p2.startswith('R'):
        posicaoOrigem = int(p2[1:])
        posicaoDestino = int(p1[1:])
        registros[posicaoDestino] += registros[posicaoOrigem]
      else:
        posicao = int(p1[1:])
        registros[posicao] += int(p2)

    elif elementos[0] == 'SUB':
      if p2.startswith('R'):
        posicaoOrigem = int(p2[1:])
        posicaoDestino = int(p1[1:])
        registros[posicaoDestino] -= registros[posicaoOrigem]
      else:
        posicao = int(p1[1:])
        registros[posicao] -= int(p2)

    elif elementos[0] == 'DIV':
      if p2.startswith('R'):
        posicao_origem = int(p2[1:])
        posicao_destino = int(p1[1:])
        if registros[posicao_origem] != 0:
          registros[posicao_destino] /= registros[posicao_origem]
        else:
          print("Erro: Divisão por zero.")
      else:
        posicao = int(p1[1:])
        if int(p2) != 0:
          registros[posicao] /= int(p2)
        else:
          print("Erro: Divisão por zero.")

    mostra_memoria()
  else:
    print("Comando inválido.")


while True:
  cmd = input('Digite o comando (ou HALT para encerrar): ')
  if cmd == 'HALT':
    break
  executar_comando(cmd)
