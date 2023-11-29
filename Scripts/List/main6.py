print('notas dos alunos')
for y in range(5):
  lista = []
  nota = []
  print (f'aluno {y+1}')
  media = 0
  nota = []

  for k in range(3):
    nota.append(int(input(f'Nota {k+1}: ')))
    media += nota[k]
    
  media = media/3
  lista.append(media)
  print(nota)
  print (lista)