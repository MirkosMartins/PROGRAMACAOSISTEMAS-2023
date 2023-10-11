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

memoria()#constroi a memoria
cmd=''
while(cmd!='HALT'):
  cmd = input('\nDigite o comando: ')
  elementos = cmd.split(' ')
  if len(elementos)==2:
    param=elementos[1].split(',')
    p1=param[0]
    p2=param[1]
    if elementos[0]=='LOAD':
      if p2.startswith('R'):
        print('\nP2 eh um registro\n')
        posicaoOrigem = int(p2[1:])
        posicaoDestino = int(p1[1:])
        registros[posicaoDestino]=registros[posicaoOrigem]
        mostraMemoria()
      else:
        posicao = int(p1[1:])
        # print("Posição:/", posicao,len(registros))
        registros[posicao]=int(p2)
        mostraMemoria()
        
#TAREFA: IMPLEMENTAR O COMANDO ADD, NO PROPRIO CODIGO DISPONIBILIZADO NESSA PASTA:
#LINK REPLIT: https://replit.com/@MatheusNoguei18/PROCESSADOR#main.py
    
    elif elementos[0] == 'ADD':
      if p2.startswith('R'):
        posicaoOrigem = int(p2[1:])
        posicaoDestino = int(p1[1:])
        registros[posicaoDestino] += registros[posicaoOrigem]
        mostraMemoria()
      else:
        posicao = int(p1[1:])
        registros[posicao] += int(p2)
        mostraMemoria()

    print('\nComando:', elementos[0], '\nParam:', elementos[1])
