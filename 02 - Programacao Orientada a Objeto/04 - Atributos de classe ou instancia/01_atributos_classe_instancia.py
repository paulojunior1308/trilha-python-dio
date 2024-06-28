class Estudante:
    # Exemplo de variavel de classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Exemplo de variavel de instancia
        self.nome = nome
        self.matricula = matricula

    def __str__ (self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
aluno_1 = Estudante("Paulo", 1)
aluno_2 = Estudante("Eduardo", 2)
mostrar_valores(aluno_1, aluno_2)

print("---------------")
Estudante.escola = "Python"
aluno_3 = Estudante("Junior", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)