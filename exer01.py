voto = candidatoA = 10
candidatoB = 20
candidatoC = 30
nulo = 98
branco = 99

voto = int(input("Por favor,digite seu voto:"))
while voto not in [10,20,30,98,99]:
  voto = int(input("Voto inválido. Por favor, digite um voto válido:"))
  
else:
  print("Voto válido.")

