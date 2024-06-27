class Cachorro:

    # Método construtor
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

        # Método destrutor
    def __dell__(self):
        print("Destruindo a instancia")    

    def falar(self):
        print("auauau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


#c = Cachorro("Chappie", "amarelo")
#c.falar()


criar_cachorro()