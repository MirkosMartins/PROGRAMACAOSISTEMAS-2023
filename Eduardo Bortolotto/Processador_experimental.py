#processador experimental
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
  cmd = input('Digite o comando:\n').upper() # EX: ADD R0,R1
  elementos = cmd.split(' ') # Elementos == ['ADD', 'R0,R1']
  if len(elementos)==2: # Conferindo se a entrada está no formato correto.
    param=elementos[1].split(',') # param == ['R0', 'R1']
    p1=param[0] # 'R0'
    p2=param[1] # 'R1'
    if elementos[0]=='LOAD': # Verificando a operação
      if p2.startswith('R'): # startswith pode retornar true or false baseado na letra inicial.
        print('P2 eh um registro')
        posicaoOrigem = int(p2[1:])
        posicaoDestino = int(p1[1:])
        registros[posicaoDestino]=registros[posicaoOrigem]
        mostraMemoria()
      else:
        # Guarda o valor de p2 no endereço p1
        posicao = int(p1[1:]) # p1 vale 'R1', p1[1:], vale '1', int(p1[1:]) vale 1.
        registros[posicao]=int(p2)
        mostraMemoria()


    elif elementos[0]=='ADD': #Conferindo se a operação é de 'ADD'
      if p2.startswith('R'):

        posicao_1 = int(p1[1:]) # indice aonde vai ser somado.
        posicao_2 = int(p2[1:]) # indice do valor que vai ser somado.

        soma = registros[posicao_1]+registros[posicao_2]
        registros[posicao_1] = soma
        mostraMemoria()

      else: # Caso não comece com 'R'.
        # acrescimo de um valor novo.
        posicao_1 = int(p1[1:]) 
        valor = int(p2)
        registros[posicao_1] += valor
        mostraMemoria()

  elif cmd!='HALT': #Exemplificando o formato de entrada correto.
    print('\nA entrada não está no formato correto digite novamente!')
    print('Ex: LOAD R0,R1 ou ADD R0,R1!\n')