frase = input("Digite uma frase:")

frase.lower()

vogais = 0
consoantes = 0

listas_vogais = "aeiou"

for char in frase:
    if "a" <= char <= "z" :
        if char in listas_vogais:
            vogais +=1
        else:
            consoantes +=1 
print(f"numeros de vogais:{vogais}")
print(f"numeros de consoantes:{consoantes}")
