total_gasto = 0.0
numero_de_despesas = 0

print("Bem-vindo ao Controle de Despesas!")
print("Digite o valor de cada despesa. Digite 0 para encerrar.")

while True:
  try:
    valor_despesa = float(input("Digite o valor da despesa: "))
  except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    continue  
  
  if valor_despesa == 0:
    break
  
  total_gasto += valor_despesa
  
  numero_de_despesas += 1

print("\n--- Resumo das Despesas ---")

if numero_de_despesas > 0:
  
  media_por_despesa = total_gasto / numero_de_despesas
  
  print(f"Total gasto: R$ {total_gasto:.2f}")
  print(f"Número de despesas registradas: {numero_de_despesas}")
  print(f"Valor médio por despesa: R$ {media_por_despesa:.2f}")
else:
  print("Nenhuma despesa foi registrada.")