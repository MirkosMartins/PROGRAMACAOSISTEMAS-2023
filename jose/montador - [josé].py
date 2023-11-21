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
linhasArquivo = []
registros = []
labels = {}

def memoria(): #monta memória
  global registros
  for i in range(10):
    registros.append(0)
  return registros

def mostraMemoria(): #mostra os valores de cada registro
    global registros
    print('[',end='')
    for i in range(len(registros) - 2):
        print(f'{registros[i]:.1f}', end=', ')
    print(f'{registros[9]:.1f}]')

def leArquivo(nomeArquivo): # mapear o arquivo (as labels e o que cada linha tem)
    global labels
    with open(nomeArquivo) as arquivo: # abre o arquivo e guarda na variável arquivo
        flagLabel = False
        for linha in arquivo:
            if flagLabel == True:
                labels[nomeLabel] = linha.split(' ')[0]
                flagLabel = False
            if linha.rstrip().endswith(':'):
                flagLabel = True
                nomeLabel = linha[:len(linha)-2]
            linhasArquivo.append(linha.rstrip().lower())
        arquivo.close()
 
def mostraLinhas():
    print("Script =========")
    global linhasArquivo
    for i in linhasArquivo:
        print(i)
    print('='*16)
        
def executa(): #faz o programa rodar apartir da main
    try:
        endMain = labels['main']
        nrLinha = 0
        print(endMain)
        for l in linhasArquivo:
            if l.startswith(endMain):
                nrLinha =  1
                break
        rep = 0
        while nrLinha != -1:
            rep += 1
            nomeLinha = ('0' if nrLinha < 10 else '') + str(nrLinha)
            for l in linhasArquivo:
                if l.startswith(nomeLinha):
                    print(l,'linha')
                    nrLinha = executaComando(l)
                    rep = 0
                    break
    except:
        print('input nao possui main\nFim do programa.',Exception.__name__)
  
def executaComando(cmd):
    elementos = cmd.split(' ')
    if len(elementos) == 3:
        if ',' in elementos[2]:
            param = elementos[2].split(',')
            p1 = param[0]
            p2 = param[1]
            posicaoDestino = int(p1[1:]) 
            if p2.startswith('r'):
                valorOrigem = registros[int(p2[1:])]
            else:
                valorOrigem = int(p2)
            if elementos[1] == 'load':
                registros[posicaoDestino] = valorOrigem
            if elementos[1] == 'add':
                registros[posicaoDestino] += valorOrigem
            if elementos[1] == 'sub':
                registros[posicaoDestino] -= valorOrigem
            if elementos[1] == 'mult':
                registros[posicaoDestino] *= valorOrigem
            if elementos[1] == 'div':
                if valorOrigem != 0:
                    registros[posicaoDestino] /= (valorOrigem)
                else:
                    print('Divisao por zero. ERRO')
                    return -1
            if elementos[1] == 'cmp':
                if registros[posicaoDestino] == valorOrigem:
                    return int(elementos[0]) + 1
                return int(elementos[0]) + 2
        else:
            if elementos[1] == 'jump':
                return int(elementos[2])
            elif elementos[1] == 'call':
                return int(labels[elementos[2]])
    if elementos[1]=='halt':
        print('FIM DO PROGRAMA.')
        return -1
    mostraMemoria()
    return int(elementos[0]) + 1      
       
def main():
    memoria() #constroi a memoria
    mostraMemoria() #mostra os valores da memória
    i = input('Digite o nome do arquivo: ')
    leArquivo(i) #mapear o arquivo (as labels e o que cada linha tem)
    mostraLinhas() #mostra código
    print(labels) #mostra dicionário com as labels
    executa() #executa o script

if __name__ == '__main__':
    main()