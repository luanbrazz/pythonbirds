class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):                            # *filhos->> qtd variavel de filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


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
