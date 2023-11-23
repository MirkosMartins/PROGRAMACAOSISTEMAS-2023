# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:08:17 2023

@author: mirkos@gmail.com - Mirkos O. Martins  
"""

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

  global linhasArquivo
  
  if len(elementos) == 3:
    
    if elementos[1] == 'CALL':
      flagLabel = False
      label = elementos[2]
      
      for f in linhasArquivo: 
        e = f.split(' ')
        if labels[label] in f: # se a chave da label existir no arq., ativa a flag
          flagLabel = True

        if flagLabel: # se flag = True, identificou uma label
          if len(e) == 1 and label not in e: # se não for a label certa, sai do laço
            break
          else: # se não, executa o comando pra linha
            executaComando(f)
      
      return int(elementos[0]) 
    
    if elementos[1] == 'JUMP':
      for c in linhasArquivo:
        e = c.split(' ')
        if elementos[2] == e[0]:
          executaComando(c)
      return int(elementos[0])

    
    param = elementos[2].split(',')
    p1 = param[0]
    p2 = param[1]
    posicaoDestino = int(p1[1:])

    if elementos[1] == 'CMP':
      cmp = False
      if p2.startswith('R'):
        if registros[posicaoDestino] == registros[int(p2[1:])]:
          cmp = True
      else:
        if registros[posicaoDestino] == int(p2):
          cmp = True

      print(f'{cmd}: {cmp}')
      
      if not cmp:
        return int(elementos[0])+1
      
      return int(elementos[0])
    
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
          registros[posicaoDestino] = registros[posicaoDestino] / registros[int(p2[1:])]
        else:
          print('Divisao por zero. ERRO')
          return -1
      else:
        if int(p2) != 0:
          registros[posicaoDestino] = registros[posicaoDestino] / int(p2)
        else:
          print('Divisao por zero. ERRO')
          return -1

    mostraMemoria()
          
  if elementos[1] == 'HALT':
    print('FIM DO PROGRAMA.')
    return -1    

  return int(elementos[0])

def executa():
  try:
    nrLinha = 0
    endMain = labels['main']
    
    for l in linhasArquivo: # p cada linha do arquivo...
      if l.startswith(endMain): # se a linha começar com o endereço do main
        nrLinha = executaComando(l)
        break
    
    while nrLinha != -1:
      nomeLinha = '0' + str(nrLinha + 1) if nrLinha <= 9 else str(nrLinha + 1)
      for l in linhasArquivo:
        if l.startswith(nomeLinha):
          nrLinha = executaComando(l)
          break     

  except IndexError : # tratando os 2 erros específicos possíveis

    contlabels = 0
    flagMain = False

    for l in linhasArquivo:
      elementos = l.split(' ')
      if len(elementos) == 1 and elementos[0].endswith(':'):
        elementos[0] = elementos[0].replace(':', '')
        # print(f'label encontrada: {elementos[0]}')
        contlabels+=1
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
        # print(f'label encontrada: {elementos[0]}')
        contlabels+=1
        if elementos[0] == 'main':
          flagMain = True

    if flagMain is False:
      print("Input nao contem main.", Exception.__name__)
      return Exception.__name__

def leArquivo(nomeArquivo): 
  global labels
  with open(nomeArquivo) as arquivo: 
    flagLabel = False # flag de leitura de label por padrão como falso
    nomeLabel = None 
    for linha in arquivo:
      elementos = linha.rstrip().split(' ')

      if flagLabel:
        labels[nomeLabel] = elementos[0]
        flagLabel = False
      if linha.rstrip().endswith(':'): # se o conteudo da linha terminar com ':' (label)
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
  print('\n')
  print(f'labels dictionary: {labels}')
  executa()
  

if __name__ == '__main__':
  main()
