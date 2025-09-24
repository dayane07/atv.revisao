luz_acesa = False

while True:
  
  print("\nO que fazer? (1: apertar interruptor, 0: sair)")
  
  escolha = input("Digite sua opção: ")
  
  if escolha == '1':
    
    luz_acesa = not luz_acesa
    
    if luz_acesa:
      print("A luz está ACESA.")
    else:
      print("A luz está APAGADA.")
  
  elif escolha == '0':
    
    print("Saindo do programa.")
    break
  
  else:
    
    print("Opção inválida. Por favor, digite '1' ou '0'.")