print('====DESAFIO 26====')

frase = input('Digite uma frase motivacional: ')
cont = frase.count('a')
primeiro = frase.find('a')
ultimo = frase.rfind('a')+1

print(f'Essa frase possue {cont} letras "a".')
print(f'O primeiro "a" da frase esta na posição {primeiro}')
print(f'O último "a" esta na posição {ultimo}')
