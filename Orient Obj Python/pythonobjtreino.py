class Cadastro:
    def __init__(self, nome, nasc, cpf, ender, npai, nmae):
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.ender = ender
        self.npai = npai
        self.nmae = nmae
    def obternome(self):
        return self.nome
    def trocanome(self, mudarnome):
        self.nome = mudarnome
    def obternasc(self):
        return self.nasc
    def trocanasc(self, mudarnasc):
        self.nasc = mudarnasc
    def obtercpf(self):
        return self.cpf
    def trocacpf(self,mudarcpf):
        self.cpf = mudarcpf
    def obterender(self):
        return self.ender
    def trocaender(self, mudarender):
        self.ender = mudarender
    def obternpai(self):
        return self.npai
    def trocanpai(self, mudarnpai):
        self.npai = mudarnpai
    def obternmae(self):
        return self.nmae
    def trocanmae(self, mudarnmae):
        self.nmae = mudarnmae
    
cad = Cadastro(input('Digite seu nome: '), input('Digite sua data de nascimento: '), input('Digite seu cpf: '), input('Digite seu endereço: '), input('Digite nome de seu pai ou responsavel: '), input('Digite nome de sua mãe ou responsavel: '))

print('Nome: ', cad.obternome())
print('Data de nascimento: ', cad.obternasc())
print('CPF: ', cad.obtercpf())
print('Endereço: ', cad.obterender())
print('Nome do pai: ', cad.obternpai())
print('Nome da mãe: ', cad.obternmae())
print('\n')

cad.trocanome(input('Novo/troca nome: '))
cad.trocanasc(input('Nova/troca data de nascimento: '))
cad.trocacpf(input('Troca cpf: '))
cad.trocaender(input('Novo/troca seu endereço: '))
cad.trocanpai(input('Novo/Troca nome do pai: '))
cad.trocanmae(input('Novo/Troca nome da mãe: '))
print('\n')

print('Nome: ', cad.obternome())
print('Data de nascimento: ', cad.obternasc())
print('CPF: ', cad.obtercpf())
print('Endereço: ', cad.obterender())
print('Nome do pai: ', cad.obternpai())
print('Nome da mãe: ', cad.obternmae())