class Pessoa:
    olhos = 2            ## Atributo default / Atributo de Classe
    def __init__(self, *filhos, nome=None, idade=35):                            # *filhos->> qtd variavel de filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    luan = Pessoa(nome ='Luan')
    edson = Pessoa(luan, nome ='Edson')
    print(Pessoa.cumprimentar(edson))
    print(id(edson))
    print(edson.cumprimentar())
    print(edson.nome)
    print(edson.idade)
    for filho in edson.filhos:
        print(filho.nome)
    edson.sobrenome = 'Braz'
    del edson.filhos
    edson.olhos = 3
    del edson.olhos
    print(edson.__dict__)
    print(luan.__dict__)
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(edson.olhos)
    print(luan.olhos)
    print(id(Pessoa.olhos), id(edson.olhos), id(luan.olhos))
    print(Pessoa.metodo_estatico(), edson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), edson.nome_e_atributos_de_classe())
