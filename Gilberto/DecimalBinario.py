
# Conversão Decimal para Binário

numero = float(input("Informe o número decimal: "))

if numero < 0:
  sinal = '-'
  numero = abs(numero)
else:
  sinal = ''

parte_inteira = int(numero)
parte_fracionaria = numero - parte_inteira

binario_inteiro = bin(parte_inteira).replace("0b", "")

binario_fracionario = ""
precisao = 4

for _ in range(precisao):
  parte_fracionaria *= 2
  bit = int(parte_fracionaria)
  binario_fracionario += str(bit)
  parte_fracionaria -= bit

resultado = f"{sinal}{binario_inteiro}.{binario_fracionario}"

print(f"Conversão: {resultado}")
