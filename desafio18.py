import math

print('===DESAFIO 17===')

c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))

teste1 = math.pow(c1 , 2)
teste2 = math.pow(c2 , 2)

h = teste1 + teste2
h2 = math.sqrt(h)
print(f'O valor da hipotenusa é: {math.trunc(h2)}')


