from biblioteca import Biblioteca as B

b1 = B("equipamentos.txt", "Menu")

menu = {'l':"listar", 'E':"emprestimo", 'A': "adicionar", 'D': "devolucão", 'S': "sair" }

op = False
while not(op == 's'):
  print(f"\n ----------{b1.nomeBiblioteca}------------\n")
  for chave, valor in menu.items():
    print(chave, ": ", valor)

  op = input("opcão: ").lower()

  if op == 'l':
    print("\n opção: listar\n")
    print('---------------lista equipamentos---------------')
    b1.imprimirEq()

  elif op == 'e':
    print("\n opção: alugar\n")
    b1.alugarEq()

  elif op == 'a':
    print("\n opção: adicionar\n")
    b1.adicionar()

  elif op == 'd':
    print("\n opção: devolução\n")
    b1.devolucao()

  elif op == 's':
    break

  else:
    continue