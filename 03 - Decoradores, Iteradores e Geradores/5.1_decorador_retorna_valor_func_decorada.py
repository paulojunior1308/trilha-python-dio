def meu_decorador(funcao):
    def envelope(*args, **kwards):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwards)
        print("Faz algo depois de executar")
        return resultado
        
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("Paulo")
print(resultado)