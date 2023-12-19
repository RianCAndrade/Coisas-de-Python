import random

print('--- SORTEIO Aleatorio ---')

print('\n')
while True:
    sort = input('Digite o seu nome : ') #nome do sorteado

    lista = ('Carro', 'Bicicleta', 'celular', 'pneus velhos') #itens a serem sorteados 

    
    lis = random.choice(lista)
    print('')
    print(f'O {sort} sorteou o {lis}')
    print('\n')
    print('----------------------------')