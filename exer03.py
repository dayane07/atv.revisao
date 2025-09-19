while True:
    try:
        n = int(input("Digite um numero inteiro positivo para calcular o fatorial: "))
        if n < 0:
            print("O fatorial não é definido para numeros negativos. Por favor, digite um numero positivo:")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um numero inteiro.")
       
if n == 0:
        fatorial = 1
else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i

print (f"O fatorial de {n} é {fatorial}")