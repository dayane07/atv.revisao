voto = candidatoA = 10
candidatoB = 20
candidatoC = 30
nulo = 98
branco = 99

voto = int(input("Por favor,digite seu voto:"))
while voto not in [10,20,30,98,99]:
  voto = int(input("Voto inválido. Por favor, digite um voto válido:"))
  
if voto == candidatoA:
  print("Voto válido, voto para candidato A")
elif voto == candidatoB:
  print("Voto válido, voto para candidato B")
elif voto == candidatoC:
  print("Voto válido, voto para candidato C")
elif voto == nulo:
  print("Válido, voto nulo")
elif voto == branco:
  print("Válido, voto branco")

else:
  print("Voto válido.")


