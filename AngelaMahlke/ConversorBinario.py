
print('╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮')
print('                 CONVERSOR DE BASES                       ')
print('╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯')
print('    --------------------------------------------------\n')
print('        OPÇÃO 1               BINARIO P/ DECIMAL \n')
print('        OPÇÃO 2               DECIMAL P/ BINARIO \n')
print('    +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+++++++++=+=+=+=+=')
print('    --------------------------------------------------')


opt = int(input('\t> '))

if (opt == 1):  # Binario pra decimal
  print("\n\tOBS.: Aceita números fracionais! (Utilizar '.')")
  vec = str(input('\tInsira o número binário: '))

  esquerda = []  # Guarda a esquerda da string separada (virgula)
  direita = []  # Guarda a direita da string separada (virgula)
  num2posi = []  # Guarda as potências de dois positivas
  num2nega = []  # Guarda as potências de dois negativas
  resp = []  # Guarda valores do(s) 1(s)

  for c in range(len(vec)):
    if vec[c] == '.':
      break
    esquerda.append(int(vec[c]))  # Coloca no vetor num os int's de vec

  indice = vec.find('.')
  result = 0

  if '.' in vec:  ####### se houver '.' no vec, ele executa o código abaixo
    for c in range(indice + 1, len(vec)):
      direita.append(int(vec[c]))

    i = 1

    while i <= len(direita):
      num2nega.append(pow(2, -i))
      i += 1

    for c in range(len(direita)):
      if direita[c] == 1:
        result += num2nega[c]

  j = len(esquerda) - 1

  while j >= 0:  ## este laço coloca cada potência de dois positiva para o tamanho da string digitada até a vírgula(se houver)
    num2posi.append(pow(2, j))
    j -= 1

  for c in range(len(esquerda)):
    if esquerda[c] == 1:  ## se o valor do binário for um, consideramos e acumulados o valor das potências, se não, continua o laço
      result += num2posi[c]
    else:
      c += 1

  print('\n\tRESPOSTA:\n    > {}'.format(result))

elif (opt == 2):  # Decimal pra binario
  opt2 = int(input("\n\tO número decimal é negativo?\n\t  1 - SIM\n\t  2 - NÃO\n\t  > "))



  if opt2 == 1:  ## se o número for negativo
    dec = str(input("\tInsira o decimal > "))
    dec = dec[1::]
    dec = int(dec)
    binario = bin(dec)
    binario = binario[2::]
    binario = str(binario)
    
    # Inverta todos os bits
    complemento = ''.join('1' if bit == '0' else '0' for bit in binario)

    # Adicionar 1 ao complemento
    sobra = 1
    numeronegativo = []

    for bit in reversed(complemento):  # Realizar as operações de soma dos binarios
      if bit == '0' and sobra == 1:  # 1 + 0 = 1
        numeronegativo += '1'
        sobra = 0
      elif bit == '1' and sobra == 1:  # 1 + 1 = 0
        numeronegativo += '0'
        sobra = 1
      else:  # caso que não tem operação
        numeronegativo += bit

      # Inverter de novo o resultado e acrescenta-se '1' no início (sinal negativo) para obter o complemento de dois

    numeronegativo = '1' + ''.join(reversed(numeronegativo))

    print(f"\n\tRESPOSTA\n    > {numeronegativo}")

  elif opt2 == 2:  ## se o número for positivo
    print("\n\tOBS.: Aceita números fracionais! (Utilizar '.')")
    dec = float(input('\tInsira o número decimal: '))
    resto = 0  # Recebe o resto por dois do dec
    restos = []  # Guarda os restos na ordem em que os obtemos ao dividir
    r = []  # Organiza os restos na ordem certa (ao contrário)

    guardaint = []  # Guarda as partes inteiras da parte fracional de dec
    resultint = 0

    decinteiro = int(dec)  # Conseguir apenas a parte inteira do número inserido pelo usuário
    restodec = dec - decinteiro  # Parte decimal do número inserido

    ## Código para a parte fracionaria
    while len(guardaint) <= 5:
      restodec = restodec * 2
      resultint = int(restodec)
      guardaint.append(str(resultint))
      restodec = restodec - int(restodec)

    ## Código para a parte inteira
    quociente = 0

    while 1:
      quociente = decinteiro // 2
      resto = decinteiro % 2
      restos.append(resto)
      decinteiro = quociente
      if quociente == 0:
        break

    i = len(restos) - 1  # Restos da parte inteira

    while i >= 0:
      r.append(str(restos[i]))
      i -= 1

    if (
        dec % 2 == 0
    ):  # se for fracionário, coloca o pontinho na resposta, se não, não coloca
      s = ''.join(
        r)  # Colocar os restos em uma única string, ao invés de lista
    else:
      s = ''.join(r) + '.'
      s += ''.join(guardaint)

    print(f'\n\tRESPOSTA\n    > {s}')

else:
  print('\tERRO')
