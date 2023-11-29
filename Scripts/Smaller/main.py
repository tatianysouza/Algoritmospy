d1={'matemática':'90', 'física':'80', 'algortimos':'85'}
menor = min(d1, key=d1.get)
print(f' A menor nota foi {menor}:', d1.get(menor))