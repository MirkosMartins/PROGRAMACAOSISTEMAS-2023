# -*- coding: utf-8 -*-
'''
[x] CMP
[x] CALL
[x] JUMP
'''

"""
Created on Wed Nov 15 22:08:17 2023

@author: mirkos@gmail.com - Mirkos O. Martins  
"""
linhasArquivo=[]
registros=[]
labels = {}

def mostraMemoria(): #mostra os valores de cada registro
  global registros
  print(registros)

def memoria(): #monta memória
  global registros
  for i in range(10):
    registros.append(0)
  return registros

def executaComando(cmd):
    elementos = cmd.split(' ')
    if len(elementos) == 3:
        if ',' in elementos[2]:
            param = elementos[2].split(',')
            #print(param)
            p1 = param[0]
            p2 = param[1]
            posicaoDestino = int(p1[1:])
            if p2.startswith('R'):
                valorOrigem = registros[int(p2[1:])]
                #print('Registro: R',p2[1:],'=',valorOrigem)            
            else:
                valorOrigem = int(p2)
            if elementos[1] == 'LOAD':
                registros[posicaoDestino]=valorOrigem
            if elementos[1] == 'ADD':
                registros[posicaoDestino]=registros[posicaoDestino]+valorOrigem
            if elementos[1] == 'SUB':
                registros[posicaoDestino]=registros[posicaoDestino]-valorOrigem
            if elementos[1] == 'MULT':
                registros[posicaoDestino]=registros[posicaoDestino]*valorOrigem
            if elementos[1] == 'DIV':
                if valorOrigem != 0:
                    registros[posicaoDestino]=int(registros[posicaoDestino]/valorOrigem)
                else:
                    print('Divisao por zero. ERRO')
                    return -1
            if elementos[1] == 'CMP':
                if registros[posicaoDestino] == valorOrigem:
                    return int(elementos[0]) + 1
                return int(elementos[0]) + 2
        else:
            if elementos[1] == 'JMP':
                return int(elementos[2])
            elif elementos[1] == 'CALL':
                return int(labels[elementos[2]])
        mostraMemoria()
    if elementos[1]=='HALT':
        print('FIM DO PROGRAMA.')
        return -1
    return int(elementos[0]) + 1      
          
def executa():
    #procura o main
    try:
        endMain = labels['main']
        nrLinha = 0
        print(endMain)
        for l in linhasArquivo:
            if l.startswith(endMain):
                nrLinha =  1
                break
        while nrLinha != -1:
            nomeLinha = ('0' if nrLinha < 10 else '') + str(nrLinha)
            for l in linhasArquivo:
                if l.startswith(nomeLinha):
                    print(l,'linha')
                    nrLinha = executaComando(l)
                    break
    except:
        print('input nao possui main\nFim do programa.',Exception.__name__)

def leArquivo(nomeArquivo): # mapear o arquivo (as labels e o que cada linha tem)
    global labels
    with open(nomeArquivo) as arquivo: # abre o arquivo e guarda na variável arquivo
        flagLabel=False
        nomeLabel=None
        for linha in arquivo:
            elementos=linha.split(' ')
            if flagLabel==True:
                labels[nomeLabel]=elementos[0]
                flagLabel=False
            if linha.rstrip().endswith(':'):
                flagLabel=True
                nomeLabel=linha[:len(linha)-2]
            linhasArquivo.append(linha.rstrip())
        arquivo.close()

def mostraLinhas():
    global linhasArquivo
    for i in linhasArquivo:
        print(i)
        
def main():
    memoria() #constroi a memoria
    mostraMemoria() #mostra os valores da memória
    i = input('Digite o nome do arquivo: ')
    leArquivo(i) #mapear o arquivo (as labels e o que cada linha tem)
    mostraLinhas() #mostra código
    print(labels) #
    executa() #

if __name__ == '__main__':
    main()