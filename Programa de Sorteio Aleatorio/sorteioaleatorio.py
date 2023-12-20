import random

print('--- SORTEIO ALEATORIO \n')

lista = ['moto', 'carro', 'geladeira', 'boneco'] # itens a serem sorteados

while True:

    sorteado = input('Digite seu nome: ') #nome do sorteado
    print('')

    if (not lista): # verificar se a lista estar vazia antes de sortear
        print('A lista estar vazia sorteio acabado =D \n')
        break

    print(f'Lista atual --->{lista}<---')

    lis = random.choice(lista)
    print('')
    print(f'========== O {sorteado} sorteou o {lis} ==========\n')

    lista.remove(lis)

    print(f'Lista apos o sorteio ===>{lista}<=== \n\n')

    print('-------------------------------------------------- ')
    print('-------------------------------------------------- \n\n')