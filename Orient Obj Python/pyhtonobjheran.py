import os
class Funcionario:
    def __init__(self, nome, idade, cpf, cad):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cad = cad
    def cargo(self):
        pass
class Pessoa1(Funcionario):
    def cargo(self):
        return 'Cirurgião(ã)'
class Pessoa2(Funcionario):
    def cargo(self):
        return 'Enfermeiro(a)'
class Pessoa3(Funcionario):
    def cargo(self):
        return 'Recepcionista'
class Pessoa4(Funcionario):
    def cargo(self):
        return 'clinico(a)'
    
print('----------Hospital---------- \n')
pe1 = Pessoa1(input('Seu Nome: '), int(input('Sua idade: ')), int(input('Seu CPF: ')), int(input('Seu n. de cadastro: ')))
os.system('cls' if os.name == 'nt' else 'clear')
pe2 = Pessoa2(input('Seu Nome: '), int(input('Sua idade: ')), int(input('Seu CPF: ')), int(input('Seu n. de cadastro: ')))
os.system('cls' if os.name == 'nt' else 'clear')
pe3 = Pessoa3(input('Seu Nome: '), int(input('Sua idade: ')), int(input('Seu CPF: ')), int(input('Seu n. de cadastro: ')))
os.system('cls' if os.name == 'nt' else 'clear')
pe4 = Pessoa4(input('Seu Nome: '), int(input('Sua idade: ')), int(input('Seu CPF: ')), int(input('Seu n. de cadastro: ')))
os.system('cls' if os.name == 'nt' else 'clear')

print(f'O Funcionario é {pe1.nome}\n Idade: {pe1.idade} \n CPF: {pe1.cpf}\n N. de cadastro: {pe1.cad}\n Profissão: {pe1.cargo()}\n')
print(f'O Funcionario é {pe2.nome}\n Idade: {pe2.idade}\n CPF: {pe2.cpf}\n N. de cadastro: {pe2.cad}\n Profissão: {pe2.cargo()}\n')
print(f'O Funcionario é {pe3.nome}\n Idade {pe3.idade}\n CPF {pe3.cpf}\n N. de cadastro: {pe3.cad}\n Profissão: {pe3.cargo()}\n')
print(f'O Funcionario é {pe4.nome}\n Idade {pe4.idade}\n CPF {pe4.cpf}\n N. de cadastro: {pe4.cad}\n Profissão: {pe4.cargo()}\n')