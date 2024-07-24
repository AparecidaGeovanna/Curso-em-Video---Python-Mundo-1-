print('===DESAFIO 29===')

velocidade = float(input('Digite a velocidade que o carro estava: '))
diferenca = velocidade-80
multa = diferenca*7.00

if velocidade >=80:
    print(f'Sua velocidade era {velocidade.__trunc__()}Km e você será multado em R${multa} reais!')
else:
    print(f'Sua velocidade era {velocidade.__trunc__()}Km e você não será multado!')