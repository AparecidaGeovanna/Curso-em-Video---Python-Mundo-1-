print('====DESAFIO 11====')

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = altura * largura
tinta = (area / 2) / 100

print(f'A área total da parede é {area}m e com isso será necessário {tinta} galões de tinta para pintar a parede toda!')