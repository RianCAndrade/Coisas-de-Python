class Pessoa:
    def __init__(self, nome, idade, cpf, ender, npai, nmae):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.ender = ender
        self.npai = npai
        self.nmae = nmae
    def olhanome(self):
        return self.nome
    def alterarnome(self, novonome):
        self.nome = novonome
    def olhaidade(self):
        return self.idade
    def alteraridade(self, novaidade):
        if(novaidade >= 0):
            self.idade = int(novaidade)
        else:
            print('Digite esse numero direito poha')
    def olhacpf(self):
        return self.cpf
    def alterarcpf(self, novocpf):
        if(novocpf >= 0):
            self.cpf = int(novocpf)
        else:
            print('Digite esse cpf direito krl')
    def olhaender(self):
        return self.ender
    def alterarender(self, novoender):
        self.ender = novoender
    def olhanpai(self):
        return self.npai
    def alterarnpai(self,novonpai):
        self.npai = novonpai
    def olhanmae(self):
        return self.nmae
    def alterarnmae(self, novanmae):
        self.nmae = novanmae
    
pcad = Pessoa('Goku', 90, 40028922, 'Planeta vegeta', 'Bardock', 'Gine')

print('NOME: ', pcad.olhanome())
print('IDADE: ', pcad.olhaidade())
print('CPF: ', pcad.olhacpf())
print('ENDEREÇO: ', pcad.olhaender())
print('NOME DO PAI: ', pcad.olhanpai())
print('NOME DA MÃE: ', pcad.olhanmae())

pcad.alterarnome('Clebis Azeite')
pcad.alteraridade(32)
pcad.alterarcpf(90029309155)
pcad.alterarender('Rua bosta')
pcad.alterarnpai('Inexistente')
pcad.alterarnmae('Ivete Sangalo')
print('\n')

print('NOME: ', pcad.olhanome())
print('IDADE: ', pcad.olhaidade())
print('CPF: ', pcad.olhacpf())
print('ENDEREÇO: ', pcad.olhaender())
print('NOME DO PAI: ', pcad.olhanpai())
print('NOME DA MÃE:', pcad.olhanmae())