import datetime

class Biblioteca:
  def __init__ (self, listaInstrumentos, nomeBiblioteca):
    self.listaInstrumentos = listaInstrumentos 
    self.nomeBiblioteca = nomeBiblioteca
    self.instrumentoD = {}

    with open(self.listaInstrumentos) as instrumento:
      conteudo = instrumento.readlines()
    id = 1000
    for i in conteudo:
      self.instrumentoD.update({str(id):{"instrumento": i.replace('\n',''), "nomeAlug": '', "dataAlug": '', "estado": 'disponivel'  }})
      id = id + 1 

  def imprimirEq(self):
    for chave, valor in self.instrumentoD.items():
      print( ' id', "\t\t\t", 'nome',  "\t\t\t", 'estado')
      print('------------------------------------------------')
      print(f'{chave} \t\t\t {valor.get("instrumento")} \t\t [{valor.get("estado")}]')  
      print('')
      print('------------------------------------------------')

  def alugarEq(self):
    idEq = input('Informe o id do equipamento: ')
    dataAtual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if idEq in self.instrumentoD.keys():
      if not (self.instrumentoD[idEq]["estado"] == "disponivel"):
        print(f"Esse equipamento já foi alugado")
        return self.alugarEq()
      elif self.instrumentoD[idEq]["estado"] == "disponivel":
        nome = input('Informe o nome do equipamento: ')
        self.instrumentoD[idEq]["nomeAlug"] = nome
        self.instrumentoD[idEq]["dataAlug"] = dataAtual
        self.instrumentoD[idEq]["estado"] = "indisponivel"
        print('Empréstimo Realizado!!!')
    else:
      print('equipamento não encontrado')
      return self.alugarEq()

  def adicionar(self):
    nomeEq = input('Informe o nome do equipamento: ')
    if nomeEq == '':
      return self.adicionar()
    else:
      with open(self.listaInstrumentos, 'a') as instrumento:
        instrumento.writelines(f'{nomeEq}\n')
        self.instrumentoD.update({str(int(max(self.instrumentoD))+1):{"instrumento":    nomeEq , "nomeAlug": '', "dataAlug": '', "estado": 'disponivel'}})
        print(f'O equipamento "{nomeEq}" foi adicionado!!!')

  def devolucao (self):
    idEq = input('informe o ID do equipamento: ')
    if idEq in self.instrumentoD.keys():
      if self.instrumentoD[idEq]["estado"] == 'disponivel':
        print('Este equipamento não foi emprestado, verifique o iD!')
        return self.devolucao()
      elif not self.instrumentoD[idEq]["estado"] == "disponivel":
        self.instrumentoD[idEq]["nomeAlug"] = ''
        self.instrumentoD[idEq]["dataAlug"] = ''
        self.instrumentoD[idEq]["estado"] = "disponivel"
        print('Devolução Realizada!!!')
    else:
      print('ID não encontrado')
