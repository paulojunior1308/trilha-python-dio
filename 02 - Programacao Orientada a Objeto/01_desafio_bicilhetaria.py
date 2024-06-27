class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Bi Bi Bi")

    def parar(self):
        print("Freiando a bicicleta")

    def correr(self):
        print("Correndo com a bicicleta")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")

        def _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else:
                print("não foi possivel trocar de marcha...")

 #   def __str__(self):
 #       return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


bicicleta_1 = Bicicleta("vermelha", "caloi", 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.correr()
bicicleta_1.parar()

print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)

bicicleta_2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(bicicleta_2)
print(bicicleta_2)