palavra = input("Insira uma palavra: ")

palavraLower = palavra.lower()
palavraInversa = palavraLower[::-1]

if palavraLower == palavraInversa:
  print("Palavra palindromo!")
else:
  print("Palavra nao eh palindromo!")


