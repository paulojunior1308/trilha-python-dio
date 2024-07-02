def meu_decorador(funcao):
    def envelope(*args, **kwards):
        print("Faz algo antes de executar")
        funcao(*args, **kwards)
        print("Faz algo depois de executar")
        
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")


ola_mundo("Paulo")