from pessoaimc import PessoaIMC as P

p1 = P()
p0 = P()
d = input('Digite seu nome: ')
a = float(input('digite seu peso: ' )) 
b = float(input('Digite sua altura: '))
c = input('Digite a data de nascimento: ') 
p0.peso = a
p0.altura = b
p1.calculaIMC(p0.peso, p0.altura)
p2 = P()
x = (p1.imc)
p2.resultIMC(d, c, a, b, x )