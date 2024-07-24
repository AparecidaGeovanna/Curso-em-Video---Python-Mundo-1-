import random

print('===DESAFIO 28====')

n = int((random.randint(0, 5)))
teste = int(input('Digite o número que voce acha que o computador gerou: '))
print(f'O número digitado pelo computador foi {n}')

if teste == n:
    print(f'Parabéns! Você acertou!')
else:
    print('Você errou! Quem sabe na proxima.')