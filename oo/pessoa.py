class Pessoa:
    olhos = 2            ## Atributo default / Atributo de Classe
    def __init__(self, *filhos, nome=None, idade=35):                            # *filhos->> qtd variavel de filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}!'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai} Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    luan = Mutante(nome ='Luan')
    edson = Homem(luan, nome ='Edson')
    print(Pessoa.cumprimentar(edson))
    print(id(edson))
    print(edson.cumprimentar())
    print(edson.nome)
    print(edson.idade)
    for filho in edson.filhos:
        print(filho.nome)
    edson.sobrenome = 'Braz'
    del edson.filhos
    edson.olhos = 2
    del edson.olhos
    print(edson.__dict__)
    print(luan.__dict__)
    print(Pessoa.olhos)
    print(edson.olhos)
    print(luan.olhos)
    print(id(Pessoa.olhos), id(edson.olhos), id(luan.olhos))
    print(Pessoa.metodo_estatico(), edson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), edson.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))  #obj pessoa é uma instancia da classe Pessoa? true
    print(isinstance(pessoa, Homem))   #false
    print(isinstance(luan, Pessoa))   #true
    print(isinstance(luan, Homem))   #true
    print(luan.olhos)
    print(edson.cumprimentar())
    print(luan.cumprimentar())

