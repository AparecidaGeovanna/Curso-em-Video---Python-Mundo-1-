import random

print('====DESAFIO 19====')

aluno1 = input('Digite o nome do 1° aluno: ')
aluno2 = input('Digite o nome do 2° aluno: ')
aluno3 = input('Digite o nome do 3° aluno: ')
aluno4 = input('Digite o nome do 4° aluno: ')

pessoas = aluno1, aluno2, aluno3, aluno4
sorteio = random.choice(pessoas)

print('O aluno sorteado foi:', sorteio)


