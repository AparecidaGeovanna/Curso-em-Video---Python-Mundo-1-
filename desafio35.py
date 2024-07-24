print('====DESAFIO 34====')

salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    porc = salario * 0.10
    atual = salario + porc
    print(f'O seu salário com o aumento de 10% fica: R${atual}')
else:
    porc = salario * 0.15
    atual = salario + porc
    print(f'Seu salário com o aumento de 15% fica: R${atual}')
