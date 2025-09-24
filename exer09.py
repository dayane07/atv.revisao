criancas = 0
adolescentes = 0
adultos = 0
idosos = 0

print("Vamos classificar a idade de 10 pessoas.")

for i in range(1, 11):
  while True:
    try:
      
      idade = int(input(f"Digite a idade da {i}ª pessoa: "))
      
      if idade < 0:
        print("Idade não pode ser negativa. Tente novamente.")
        continue
      
      break  
    
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

  if 0 <= idade <= 12:
    criancas += 1
  elif 13 <= idade <= 17:
    adolescentes += 1
  elif 18 <= idade <= 59:
    adultos += 1
  else: 
    idosos += 1

print("\n--- Resumo por Categoria ---")
print(f"Crianças (0-12 anos): {criancas}")
print(f"Adolescentes (13-17 anos): {adolescentes}")
print(f"Adultos (18-59 anos): {adultos}")
print(f"Idosos (60+ anos): {idosos}")