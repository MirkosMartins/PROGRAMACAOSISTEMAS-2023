def converter_inteiro(inteiro): #Define função
    txt = ''

    if (inteiro < 0): #if serve para inverter valores negativos
        inteiro = -inteiro

    while (True): #Executa até a condição abaixo
        if (inteiro == 0):
            break # 0 = parar
        resto = inteiro % 2
        inteiro //= 2
        txt = str(resto) + txt

    if txt == '': #Se a str for vazia adiciona um 0
        txt = str(0)

    return txt #Retorna o valor

entrada = float(input()) #Digitar número decimal (entrada)

if entrada == int(entrada): #A entrada é um número inteiro 
    binario = converter_inteiro(int(entrada))
    if entrada >= 0:
        print(binario)
    else: #Entrada negativa
        binario = binario.zfill(8) #Preenche com zeros até ficar 8 unidades
        binario = '1' + binario[1:] #Binario recebe str '1' mais os numeros do indice 1 pra frente
        print(binario)
else: #A entrada é um float
    parte_int = int(entrada)
    binario = converter_inteiro(parte_int)

    if entrada < 0: #if para entrada menor que 0
        parte_fraq =  (-entrada) + parte_int 

        binario = binario.zfill(8)
        binario = '1' + binario[1:]
    else: #else para maior que 0
        parte_fraq =  entrada - parte_int
        
    txt = ''

    for i in range(10): #Converter parte fracionada
        parte_fraq *= 2
        parte_int = int(parte_fraq)
        txt = txt + str(parte_int)
        
        parte_fraq -= parte_int

    print(binario+'.'+txt)



    