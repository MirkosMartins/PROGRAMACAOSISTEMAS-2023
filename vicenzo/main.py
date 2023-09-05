num = float(input("Digite um número decimal: "))

if num < 0:
    sinal = '-'
    num = abs(num)
else:
    sinal = ''

parteInt = int(num)
parteFrac = num - parteInt

binarioInt = bin(parteInt).replace("0b", "")
binarioFunc = ""

for _ in range(8):  
    parteFrac *= 2
    bit = int(parteFrac)
    binarioFrac += str(bit)
    parteFrac -= bit

resultado = f"{sinal}{binarioInt}.{binarioFrac}"

print(f"Número binário: {resultado}")
