class Passaro:
    def voar(self):
        print("Voando ... ")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Aveztruz não voa")

def plano_de_voo(passaro):
    passaro.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)