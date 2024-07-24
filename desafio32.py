print('===DESAFIO 31===')

distancia = float(input('Digite a distância da viajem em Km: '))

if distancia <=200:
    pp = distancia*0.50
    print(f'Por se tratar de uma viajem menor que 200Km, o preço da passagem é {pp} reais.')
if distancia >200:
    pp = distancia*0.45
    print(f'Por se tratar de uma viajem maior que 200Km, o preço da passagem é {pp} reais.')