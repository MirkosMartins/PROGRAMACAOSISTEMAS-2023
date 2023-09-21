# Palíndromo

palavra = input("Digite a palavra: ")

palavraLower = palavra.lower()
palavraInvertida = palavraLower[::-1]

if palavraLower == palavraInvertida:
  print("\n✔ É um palíndromo.")

else:

  print("\n✖ Não é um palíndromo.")
