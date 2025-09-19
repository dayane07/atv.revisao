total = 0

print("Seja bem-vindo(a) ao nosso supermercado")
print("Digite o preço do produto desejado. para encerrar e ver o total digite 0")

while True:
  try:
    preço = float(input("digite o preço do produto:"))

    if preço < 0:
     print("Preço inválido, por favor digite um valor não negativo")
     continue

    if preço == 0:
     break

    total += preço
  except ValueError:
   print("Entrada inválida. Por favor, digite um número.")

print(f"---")
print(f"O valor total da sua compra é: R${total:.2f}")
