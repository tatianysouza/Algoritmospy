#
class PessoaIMC:
  peso = 0.0
  altura = 0.0

  def __unit__ (self, peso, altura):
    self.peso = peso
    self.altura = altura

  def calculaIMC(self, peso, altura):
    self.peso = peso
    self.altura = altura
    imc = peso/altura**2
    print(imc)
    self.imc = imc

  def resultIMC(self, nome, data, peso, altura, situacao ):
    print('Nome:',nome)
    print('Data de nascimento: ',data)
    print('Peso:',peso)
    print('Altura:',altura)
    if 16.0 <= situacao and 16.99 >=situacao :
      print('Situação: Baixo peso grau II')
    elif 17.0 <= situacao and 18.49 >=situacao :
      print('Situação: Baixo peso grau I')
    elif 18.50 <= situacao and 24.99 >=situacao :
      print('Situação: Peso ideal')
    elif 25.0 <= situacao and 29.99 >=situacao :
      print('Situação: Sobrepeso')
    elif 30.0 <= situacao and 34.99 >=situacao :
      print('Situação: Obesidade grau I')
    elif 35.0 <= situacao and 39.99 >=situacao :
      print('Situação: Obesidade grau II')
    return