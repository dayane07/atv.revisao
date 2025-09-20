saldo = 0

while True:
    print("\nBem-vindo(a) ao caixa eletrônico.")
    print("1. ver saldo")
    print("2. fazer deposito")
    print("3. fazer saque")
    print("0. sair")

    opçao = input("digite sua opção desejada:")
    
    if opçao == "1":
        print(f"seu saldo é:R${saldo:.2f}")
    elif opçao == "2":
        valor_deposito = float(input("digite o valor do deposito:"))
        if valor_deposito > 0:
            saldo += valor_deposito
            print("deposito realizado com sucesso.")
        else:
            print("valor de deposito inválido")
    elif opçao =="3":
     Valor_saque = float(input("digite o valor que deseja sacar:"))
     if 0 < Valor_saque >= saldo:
         saldo -= Valor_saque
         print("saque realizado com sucesso.")
     else:
         ("saldo insuficiente ou valor de saque inválido.")
    elif opçao == "0":
     print ("obrigada por usar nossos serviços, volte sempre.")
     break
    else:
       print("opção inválida. por favor, escolha umas das opções do menu.")