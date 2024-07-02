def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros = [1, 2, 3]):
    print(i)




##### EXEMPLO DE GERADORES #####
#import requests
#
#def fetch_products(api_url, max_pages = 100):
#    page = 1
#    while page <= max_pages:
#        response = requests.get(f"{api_url}?page={page}")
#        data = response.json()
#        for product in data['products']:
#            yield product
#
#        if 'next_page' not in data:
#            break
#        page += 1
#
## Uso do gerador
#for product in fetch_products("http://api.example.com/products"):
#    print(product['name'])