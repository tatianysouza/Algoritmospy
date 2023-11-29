alunos = {}
for _ in range(3):
  nome = input('Informe o nome: ')
  notas = list()
  media = 0
  for i in range(4):
    notas.append(int(input('Informe a nota: ')))
    media += notas[i]
  media = media/4
  alunos[nome] = media

print(alunos)