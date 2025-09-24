alguem_reprovou = False

print("Bem-vindo ao Verificador de Turma.")

for i in range(1, 6):
  while True:
    try:
      nota = float(input(f"Digite a nota do {i}º aluno (0 a 10): "))
      
      if 0 <= nota <= 10:
        if nota < 5.0:
          alguem_reprovou = True
        break
      else:
        print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")

if alguem_reprovou:
  print("A turma possui pelo menos um aluno reprovado.")
else:
  print("Parabéns! Todos na turma foram aprovados.")