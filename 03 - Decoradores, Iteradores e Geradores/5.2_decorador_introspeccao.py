import functools
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwards):
        funcao(*args, **kwards)
        
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")


print(ola_mundo.__name__)