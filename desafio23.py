print('====DESAFIO 22====')

nome = input('Digite seu nome completo: ')

print(f'Seu nome é {nome}')

#NOME EM MAIUSCULO
print(nome.upper())

#NOME EM MINUSCULO
print(nome.lower())

#CONTAGEM DE TODAS AS LETRAS DESCONSIDERANDO OS ESPACOS
nome2 = nome.replace(' ', '')
print(len(nome2))

#CONTAGEM DA QUANTIDADE DE LETRAS DO PRIMEIRO NOME
nome3 = nome.split()
nome4 = nome3[0]
print(len(nome4))

